from audioop import add

from Components.MEM import MEM
from Components.opcodes import *


class CPU:
    cycles: int

    def __init__(self, memory:MEM):
        self.reset(memory)

    def reset(self, memory:MEM):
        self.SP = 0x0100 # Program counter
        self.PC = 0xFFFC # Stack Pointer
        # Registers
        self.AC = 0 # Accumulator
        self.X  = 0 # X Register
        self.Y  = 0 # Y Register
        # Status flags
        self.C  = 0 # Carry
        self.Z  = 0 # Zero
        self.I  = 0 # Interrupt
        self.D  = 0 # Decimal
        self.B  = 0 # Break
        self.V  = 0 # Overflow
        self.N  = 0 # Negative
        # Initialising the memory
        memory.Init()

    def lda_set_status(self):
        self.Z = 1 if self.AC == 0 else 0
        # N = 1 only if the 7th bit of A is set
        self.N = 1 if (self.AC and 0b10000000) > 0 else 0

    def fetch_byte(self, memory:MEM) -> int:
        value:int = memory.get_memory[self.PC]
        self.PC += 1
        self.cycles -= 1
        return value
    
    def read_byte(self, address:str, memory:MEM) -> int:
        value:int = memory.get_memory[address]
        self.cycles -= 1
        return value

    def fetch_word(self, memory:MEM) -> str:
        # 6502 is little endian
        value:str = memory.get_memory[self.PC]
        self.PC += 1
        value |= (memory.get_memory[self.PC] << 8)
        self.PC += 1
        self.cycles -= 2
        return value
    
    def read_word(self, address:str, memory:MEM) -> int:
        low_byte:int = self.read_byte(address, memory)
        high_byte:int = self.read_byte(address+1, memory)
        return low_byte | (high_byte << 8)

    def execute(self, cycles:int, memory:MEM):
        self.cycles = cycles
        while self.cycles > 0:
            instruction:int = self.fetch_byte(memory)

            if instruction == INS_LDA_IM:
                self.AC = self.fetch_byte(memory)
                self.lda_set_status()

            if instruction == INS_LDA_ZP:
                zp_address:int = self.fetch_byte(memory)
                self.AC = self.read_byte(zp_address, memory)
                self.lda_set_status()
            
            if instruction == INS_LDA_ZPX:
                zp_address:int = self.fetch_byte(memory)
                zp_address += self.X
                self.cycles -= 1
                self.AC = self.read_byte(zp_address, memory)
                self.lda_set_status()

            if instruction == INS_LDA_AB:
                abs_address:str = self.fetch_word(memory)
                self.AC = self.read_byte(abs_address, memory)

            if instruction == INS_LDA_ABX:
                abs_address:str = self.fetch_word(memory)
                abs_address_x:str = abs_address + self.X
                self.AC = self.read_byte(abs_address_x, memory)
                if abs_address_x - abs_address >= 0xFF:
                    self.cycles -= 1

            if instruction == INS_LDA_ABY:
                abs_address:str = self.fetch_word(memory)
                abs_address_y:str = abs_address + self.Y
                self.AC = self.read_byte(abs_address_y, memory)
                if abs_address_y - abs_address >= 0xFF:
                    self.cycles -= 1
            
            if instruction == INS_LDA_INX:
                zp_address:int = self.fetch_byte(memory)
                zp_address += self.X
                self.cycles -= 1
                effective_address:str = self.read_word(zp_address, memory)
                self.AC = self.read_byte(effective_address, memory)

            if instruction == INS_LDA_INY:
                zp_address:str = self.fetch_byte(memory)
                effective_address:str = self.read_word(zp_address, memory)
                effective_address_y:str = effective_address + self.Y
                self.AC = self.read_byte(effective_address_y, memory)
                if effective_address_y - effective_address >= 0xFF:
                    self.cycles -= 1

            if (instruction == INS_JSR):
                jsr_address:str = self.fetch_word(memory)
                memory.write_word(self.PC - 1, self.SP)
                self.cycles -= 2
                self.SP += 2
                self.PC = jsr_address
                self.cycles -= 1

    def get_status(self):
        print("===============================================")
        print("Registers: ")
        print(f"PC: {hex(self.PC)} | SP: {hex(self.SP)}")
        print(f"AC: {hex(self.AC)} | X: {hex(self.X)} | Y: {hex(self.Y)}")
        print("\nStatus flags: ")
        print(f"C: {self.C} | Z: {self.Z} | I: {self.I} | D: {self.D} | B: {self.B} | V: {self.V} | N: {self.N}")
        print("===============================================")
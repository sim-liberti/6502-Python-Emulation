from Components.opcodes import *
from Testing.expect import *

## IMMIDIATE MODE TESTING ##########################
def LDA_IMMIDIATE_CanLoadValueIntoTheARegister(mem, cpu):
    ## Given: ##
    mem.get_memory[0xFFFC] = INS_LDA_IM #A9
    mem.get_memory[0xFFFD] = 0x42
    ## When:  ##
    cpu.execute(cycles=2, memory=mem)
    ## Then:  ##
    EXPECT_EQ(cpu.AC, 0x42)
    EXPECT_FALSE(cpu.Z)
    EXPECT_TRUE(cpu.N)
    cpu.reset(mem)
####################################################

## ZERO PAGE TESTING ###############################
def LDA_ZEROPAGE_CanLoadValueIntoTheARegister(mem, cpu):
    # Given: ##
    mem.get_memory[0xFFFC] = INS_LDA_ZP #A5
    mem.get_memory[0xFFFD] = 0x42
    mem.get_memory[0x0042] = 0x37
    # When:  ##
    cpu.execute(cycles=3, memory=mem)
    # Then:  ##
    EXPECT_EQ(cpu.AC, 0x37)
    EXPECT_FALSE(cpu.Z)
    EXPECT_TRUE(cpu.N)
    cpu.reset(mem)
####################################################

## ZERO PAGE, X TESTING ############################
def LDA_ZEROPAGEX_CanLoadValueIntoTheARegister(mem, cpu):
    ## Given: ##
    cpu.X = 2
    mem.get_memory[0xFFFC] = INS_LDA_ZPX #B5
    mem.get_memory[0xFFFD] = 0x80
    mem.get_memory[0x0082] = 0x45
    # When:  ##
    cpu.execute(cycles=4, memory=mem)
    # Then:  ##     
    EXPECT_EQ(cpu.AC, 0x45)
    EXPECT_FALSE(cpu.Z)
    EXPECT_TRUE(cpu.N)
    cpu.reset(mem)
####################################################

## ABSOLUTE TESTING ################################
def LDA_ABSOLUTE_CanLoadValueIntoTheARegister(mem, cpu):
    ## Given: ##
    mem.get_memory[0xFFFC] = INS_LDA_AB
    mem.get_memory[0xFFFD] = 0x80
    mem.get_memory[0xFFFE] = 0x44 # 0x4480
    mem.get_memory[0x4480] = 0x37 
    ## When:  ##
    cpu.execute(cycles=4, memory=mem)
    ## Then:  ##
    EXPECT_EQ(cpu.AC, 0x37)
    EXPECT_FALSE(cpu.Z)
    EXPECT_FALSE(cpu.N)
    cpu.reset(mem)
####################################################

## ABSOLUTE X TESTING ##############################
def LDA_ABSOLUTEX_CanLoadValueIntoTheARegister(mem, cpu):
    ## Given: ##
    cpu.X = 1
    mem.get_memory[0xFFFC] = INS_LDA_ABX
    mem.get_memory[0xFFFD] = 0x80
    mem.get_memory[0xFFFE] = 0x44 # 0x4480
    mem.get_memory[0x4481] = 0x37 
    ## When:  ##
    cpu.execute(cycles=4, memory=mem)
    ## Then:  ##
    EXPECT_EQ(cpu.AC, 0x37)
    EXPECT_FALSE(cpu.Z)
    EXPECT_FALSE(cpu.N)
    cpu.reset(mem)
####################################################

## ABSOLUTE Y TESTING ##############################
def LDA_ABSOLUTEY_CanLoadValueIntoTheARegister(mem, cpu):
    ## Given: ##
    cpu.Y = 1
    mem.get_memory[0xFFFC] = INS_LDA_ABY
    mem.get_memory[0xFFFD] = 0x80
    mem.get_memory[0xFFFE] = 0x44 # 0x4480
    mem.get_memory[0x4481] = 0x37 
    ## When:  ##
    cpu.execute(cycles=4, memory=mem)
    ## Then:  ##
    EXPECT_EQ(cpu.AC, 0x37)
    EXPECT_FALSE(cpu.Z)
    EXPECT_FALSE(cpu.N)
    cpu.reset(mem)
####################################################

## INDIRECT X TESTING ##############################
def LDA_INDIRECTX_CanLoadValueIntoTheARegister(mem, cpu):
    ## Given: ##
    cpu.X = 0x04
    mem.get_memory[0xFFFC] = INS_LDA_INX
    mem.get_memory[0xFFFD] = 0x02
    mem.get_memory[0x0006] = 0x00 #0x2 + 0x4
    mem.get_memory[0x0007] = 0x80
    mem.get_memory[0x8000] = 0x37
    ## When:  ##
    cpu.execute(cycles=6, memory=mem)
    ## Then:  ##
    EXPECT_EQ(cpu.AC, 0x37)
    EXPECT_FALSE(cpu.Z)
    EXPECT_FALSE(cpu.N)
    cpu.reset(mem)
####################################################

## INDIRECT Y TESTING ##############################
def LDA_INDIRECTY_CanLoadValueIntoTheARegister(mem, cpu):
    ## Given: ##
    cpu.Y = 0x04
    mem.get_memory[0xFFFC] = INS_LDA_INY
    mem.get_memory[0xFFFD] = 0x02
    mem.get_memory[0x0002] = 0x00
    mem.get_memory[0x0003] = 0x80
    mem.get_memory[0x8004] = 0x37 #0x8000 + 0x4
    ## When:  ##
    cpu.execute(cycles=5, memory=mem)
    ## Then:  ##
    EXPECT_EQ(cpu.AC, 0x37)
    EXPECT_FALSE(cpu.Z)
    EXPECT_FALSE(cpu.N)
    cpu.reset(mem)
####################################################
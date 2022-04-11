MAX_MEM = 1024*64

class MEM:
    def Init(self):
        self.Data = [0]*MAX_MEM

    @property
    def get_memory(self):
        return self.Data       

    def write_word(self, value:str, address:int):
        self.Data[address]   = value & 0xFF
        self.Data[address+1] = (value >> 8) 
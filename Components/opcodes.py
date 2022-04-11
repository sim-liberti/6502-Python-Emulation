## Load Accumulator Instruction Set ##
INS_LDA_IM :int = 0xA9 # Immidiate
INS_LDA_ZP :int = 0xA5 # Zero Page
INS_LDA_ZPX:int = 0xB5 # Zero Page X
INS_LDA_AB :int = 0xAD # Absolute
INS_LDA_ABX:int = 0xBD # Absolute X 
INS_LDA_ABY:int = 0xB9 # Absolute Y
INS_LDA_INX:int = 0xA1 # Indirect X
INS_LDA_INY:int = 0xB1 # Indirect Y 
######################################

## Jump to Subroutine Instruction ######
INS_JSR:int = 0x20 # Absolute mode ONLY
########################################
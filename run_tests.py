from rich import print

from Components.CPU import CPU
from Components.MEM import MEM
from Testing import LDA

def run_all():
    mem = MEM()
    cpu = CPU(mem)
    total = 0

    all_funcs = [
        LDA.LDA_IMMIDIATE_CanLoadValueIntoTheARegister(mem, cpu),
        LDA.LDA_ZEROPAGE_CanLoadValueIntoTheARegister(mem, cpu),
        LDA.LDA_ZEROPAGEX_CanLoadValueIntoTheARegister(mem, cpu),
        LDA.LDA_ABSOLUTE_CanLoadValueIntoTheARegister(mem, cpu),
        LDA.LDA_ABSOLUTEX_CanLoadValueIntoTheARegister(mem, cpu),
        LDA.LDA_ABSOLUTEY_CanLoadValueIntoTheARegister(mem, cpu),
        LDA.LDA_INDIRECTX_CanLoadValueIntoTheARegister(mem, cpu),
        LDA.LDA_INDIRECTY_CanLoadValueIntoTheARegister(mem, cpu),
    ]

    for func in all_funcs:
        func
        total += 1
    
    print("[turquoise2][ ---------------- ][/turquoise2]")
    print(f"[turquoise2][ {total} TESTS EXECUTED ][/turquoise2]")

if __name__ == "__main__":
    run_all()
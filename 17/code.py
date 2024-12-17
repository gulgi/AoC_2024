from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re
import numpy
from collections import OrderedDict
import time

class Part(Enum):
    One = 1,
    Two = 2

dirs = { 0: numpy.array([-1,0]), 1: numpy.array([0,-1]), 2: numpy.array([1,0]), 3: numpy.array([0,1]) }

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    A = int(file.readline().split(": ")[1])
    B = int(file.readline().split(": ")[1])
    C = int(file.readline().split(": ")[1])
    file.readline()
    program = list(map(int, file.readline().split(": ")[1].split(",")))

    print(f"A {A}  B {B}  C {C}  program {program}")

    # CODE
    num = 0

    ip = 0
    print(f"ip {ip}  ins {program[ip]}  op {program[ip+1]}   A: {A}  B: {B}  C: {C}" )
    while ip < len(program):
        time.sleep(0.001)
        instruction = program[ip]
        operand = program[ip+1]

#        print(f"ip {ip}  ins {instruction}  op {operand}   A: {A}  B: {B}  C: {C}" )
        
        def combo_rules(combo):
            if combo >= 0 and combo <= 3:
                return combo
            if combo == 4:
                return A
            if combo == 5:
                return B
            if combo == 6:
                return C
            else:
                print("ERROR  7")
                exit(1)
                return -1
            
        match instruction:
            case 0: # adv
                combo_reg = combo_rules(operand)
                denominator = 2 ** combo_reg
                A = int(A // denominator)
                ip += 2
            case 1: # bxl
                B = B ^ operand
                ip += 2
            case 2: # bst
                combo_reg = combo_rules(operand)
                B = combo_reg % 8
                ip += 2
            case 3: # jnz
                if A != 0:
                    ip = operand
                else:
                    ip += 2
            case 4: # bxc
                B = B ^ C
                ip += 2
            case 5: # out
                combo_reg = combo_rules(operand)
#                print(f"OUT {combo_reg % 8}, ")
                print(f"{combo_reg % 8},", end="")
                ip += 2
            case 6: # bdv
                combo_reg = combo_rules(operand)
                denominator = 2 ** combo_reg
                B = int(A // denominator)
                ip += 2
            case 7: # cdv
                combo_reg = combo_rules(operand)
                denominator = 2 ** combo_reg
                C = int(A // denominator)
                ip += 2
    print("")
    print(f"ip {ip}  A: {A}  B: {B}  C: {C}" )

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

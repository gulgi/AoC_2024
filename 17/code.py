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

    def combo_rules(combo, A, B, C):
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

    def run_program(A, B, C):
        ip = 0
        program_output = []
        while ip < len(program):
            instruction = program[ip]
            operand = program[ip+1]
            ip += 2
            match instruction:
                case 0: # adv
                    combo_reg = combo_rules(operand, A, B, C)
                    denominator = 2 ** combo_reg
                    A = int(A // denominator)
                case 1: # bxl
                    B = B ^ operand
                case 2: # bst
                    combo_reg = combo_rules(operand, A, B, C)
                    B = combo_reg % 8
                case 3: # jnz
                    if A != 0:
                        ip = operand
                case 4: # bxc
                    B = B ^ C
                case 5: # out
                    combo_reg = combo_rules(operand, A, B, C)
                    program_output.append(combo_reg % 8)
                case 6: # bdv
                    combo_reg = combo_rules(operand, A, B, C)
                    denominator = 2 ** combo_reg
                    B = int(A // denominator)
                case 7: # cdv
                    combo_reg = combo_rules(operand, A, B, C)
                    denominator = 2 ** combo_reg
                    C = int(A // denominator)
#        print(f"A {A}, B {B}, C {C}")
        return program_output

    if part == Part.One:
        program_output = run_program(A, B, C)
        print(*program_output, sep=",")
    else:
        # Hacky., by hand, ugliness

        start = 0
        if test:
            start = 117440-5
        start = 0o1000000000000000
        end   = 0o10000000000000000

        # 280195460414481 gives right answer; but is too high!
          # 7755302670536021 

        # Correct len:    35184372088832 <= x <    281474976710656
        # Correct len: 01000000000000000 <= x < 010000000000000000

        # Ends-1 in 0: 07000000000000000 <= x < 010000000000000000
        # Ends-2 in 3: 07400000000000000
        # Ends-3 in 5: 07450000000000000
        # Ends-4 in 5: 07454000000000000
        # Ends-5 in 7: 07454300000000000
        #     -6    4: 07454300000000000
        #     -7    4: 07454302000000000
        #     -8    1: 07454302600000000
        #     -9    3: 07454302670000000
        #    -10    0: 07454302670000000
        #    -11    5: 07454302670500000
        #    -12    7: 07454302670530000
        #    -13    3: 07454302670536000
        #    -14    1: 07454302670536000
        #    -15    4: 07454302670536020
        #    -16    2: 07454302670536021
        # 266932601404433 as well!
          # 7454302670536021
        # OUTPUT: 2,4,1,3,7,5,0,3,1,4,4,7,5,5,3,0 

        start = 0o7454302670536021

        for i in tqdm(range(start, end, 1)):
#            time.sleep(0.01)
            A = i
            B = 0
            C = 0
            program_output = run_program(A, B, C)

#            if A != 0: #% 1024 == 0:
#                print(f"A {A} {oct(A)}  {program} <> {program_output}")
            if program_output == program:
                print(f"Done!  A = {A}")
                num = A
                break


    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

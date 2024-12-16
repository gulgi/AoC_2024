from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re
import numpy
import sumpy

class Part(Enum):
    One = 1,
    Two = 2

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)

    # CODE
    num = 0
    while True:
        a_x, a_y = list(map(int, re.match("Button A: X\+(\d+), Y\+(\d+)", file.readline().strip()).groups()))
        b_x, b_y = list(map(int, re.match("Button B: X\+(\d+), Y\+(\d+)", file.readline().strip()).groups()))
        prize_x, prize_y = list(map(int, re.match("Prize: X\=(\d+), Y\=(\d+)", file.readline().strip()).groups()))
        button_presses_a, button_presses_b = 0, 0

        if part == Part.Two:
            prize_x += 10000000000000
            prize_y += 10000000000000

        break

#            print(f"{a_x} {a_y}")
#            print(f"{b_x} {b_y}")
#            print(f"{prize_x} {prize_y}")

        max_a_x_num = prize_x // a_x
        max_a_y_num = prize_y // a_y

        max_b_x_num = prize_x // b_x
        max_b_y_num = prize_y // b_y

#            print(f"prize_x {prize_x}  max_a_num {max_a_x_num}, {max_a_y_num}  max_b_num {max_b_x_num}, {max_b_y_num}  ")

        def find_number():
            tries_2 = 0
            mod_numbers = [set(),set()]
            for a_num_x in range(max_a_x_num, -1, -1):
                #print(f"a_num_x {a_num_x}")
                sum_a = a_num_x*a_x
                remaining = prize_x - sum_a
                b_num_x = remaining // b_x
                mod = remaining % b_x
                mod_numbers[tries_2].add(mod)
                print(f"{mod} ", end="")
                sum_b = b_num_x * b_x
                x_sum = sum_a + sum_b
                if x_sum == prize_x:
                    tries_2 = (tries_2+1) % 2
                    y_sum = a_num_x*a_y + b_num_x*b_y
                    if y_sum == prize_y:
                        return a_num_x, b_num_x
                    print(f"\nSum X works! {sum_a} + {sum_b} => {x_sum}      y_sum {y_sum} Y does not.")
                    print(f"{mod_numbers[0]}  <>    {mod_numbers[1]}")
                    if mod_numbers[0] is mod_numbers[1]:
                        return -1, -1
                    mod_numbers[tries_2] = set()
            return -1, -1

        print(f"Find number ... mod: ", end="")
        a, b = find_number()
        print(f".\nFind number DONE.")
        if a >= 0:
            print(f"Found it {a} {b}")
            num += a*3 + b*1
        else:
            print(f"NOT found")

        empty = file.readline()
        if empty == "":
            break

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

# too low 29484

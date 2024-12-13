from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re

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
    if part == Part.One:
        while True:
            a_x, a_y = re.match("Button A: X\+(\d+), Y\+(\d+)", file.readline().strip()).groups()
            b_x, b_y = re.match("Button B: X\+(\d+), Y\+(\d+)", file.readline().strip()).groups()
            prize_x, prize_y = re.match("Prize: X\=(\d+), Y\=(\d+)", file.readline().strip()).groups()
            button_presses_a, button_presses_b = 0, 0
#        print(f"{a_x} {a_y}")
#        print(f"{b_x} {b_y}")
#        print(f"{prize_x} {prize_y}")




            empty = file.readline()
            if empty == "":
                break

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

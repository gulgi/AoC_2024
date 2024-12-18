from enum import Enum
import sys
import re
import sympy

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

        if part == Part.Two:
            prize_x += 10000000000000
            prize_y += 10000000000000

        a, b = sympy.symbols('a b', integer=True)

        equation0 = sympy.Eq(a * a_x + b * b_x, prize_x)
        equation1 = sympy.Eq(a * a_y + b * b_y, prize_y)
        answer = sympy.solve([equation0, equation1], (a, b))
        if a in answer:
            num += answer[a]*3 + answer[b]
            #print(f"answer {answer}")

        empty = file.readline()
        if empty == "":
            break

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

from enum import Enum
import sys
import re

class Part(Enum):
    One = 1,
    Two = 2

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False

    # Read in file
    file = open("test.txt" if test else "input.txt")
    input = file.read()

    # CODE
    match_string = "mul\\((\\d{1,4})\\,(\\d{1,4})\\)"
    num = 0
    if part != Part.One:
        all = re.findall(match_string, input)
        for first, second in all:
            num += int(first)*int(second)
    else:
        index = 0
        while True:
            index1 = input.find("don't()", index)
            all = None
            if index1 == -1:
                all = re.findall(match_string, input[index:])
            else:
                all = re.findall(match_string, input[index:index1])
            for first, second in all:
                num += int(first)*int(second)

            if index1 == -1:
                break

            index1 = input.find("do()", index1+7)
            if index1 == -1:
                break
            index = index1

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
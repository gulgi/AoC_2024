from enum import Enum
import sys
from functools import cache

class Part(Enum):
    One = 1,
    Two = 2

def main():
    global width

    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    towels,data = file.read().split("\n\n")
    towels = towels.split(", ")
    towels.sort(key=lambda s: len(s), reverse=True)
    designs = data.split("\n")

    @cache
    def count_designs(design):
        if len(design) == 0:
            return 1
        count = 0
        for towel in towels:
            if design.startswith(towel):
                count += count_designs(design.removeprefix(towel))
        return count

    num = 0
    if part == Part.One:
        for design in designs:
            if count_designs(design) > 0:
                num += 1
    else:
        for design in designs:
            num += count_designs(design)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Result: ", num)

if __name__=="__main__":
    main()

# 75 just straight on. Too low, obviusly. Had to try.
# 97 is wrong ... :/
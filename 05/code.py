from enum import Enum
import sys
from functools import cmp_to_key

class Part(Enum):
    One = 1,
    Two = 2

def read_rules(file):
    rules = {}
    data = file.readline()
    while len(data) > 2:
        key, value = list(map(int, map(str.strip, data.split("|"))))
        rules.setdefault(key, [value]).append(value)
        data = file.readline()
    return rules

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False

    # Read in file
    file = open("test.txt" if test else "input.txt")
    rules = read_rules(file)
    lines = file.readlines()

    # Sort function. Here so we don't have to make rules global
    comp = lambda i1, i2: -1 if i1 in rules and i2 in rules[i1] else 1 if i2 in rules and i1 in rules[i2] else 0

    # CODE
    num = 0
    for line in lines:
        pages = list(map(int, line.strip().split(',')))
        corrected = sorted(pages, key=cmp_to_key(comp))
        if (part == Part.One and corrected == pages) or (part == Part.Two and corrected != pages):
            num += corrected[len(corrected) // 2]

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
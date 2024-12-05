from enum import Enum
import sys
import re
from itertools import permutations
from functools import cmp_to_key

rules = {}

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

def compare_to_rules(item1, item2):
    if item1 in rules and item2 in rules[item1]:
        return -1
    if item2 in rules and item1 in rules[item2]:
        return 1
    return 0

def main():
    global rules

    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False

    # Read in file
    file = open("test.txt" if test else "input.txt")
    rules = read_rules(file)
    lines = file.readlines()

    # CODE
    num = 0
    for line in lines:
        pages = list(map(int, line.strip().split(',')))

        corrected = sorted(pages, key=cmp_to_key(compare_to_rules))
        if part == Part.One and corrected == pages:
            num += corrected[ int(len(corrected)/2)]
        elif part == Part.Two and corrected != pages:
            num += corrected[ int(len(corrected)/2)]

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
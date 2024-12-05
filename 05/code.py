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
    while True:
        data = file.readline()
        if len(data) < 2:
            return rules
        data = data.split("|")
        key = int(data[0])
        value = int(data[1].strip())

        if key not in rules:
            rules[key] = [value]
        else:
            rules[key].append(value)

def update_ok(pages, rules):
    for i in range(0, len(pages)):
        page = pages[i]
        if page in rules:
            for rule in rules[page]:
                if rule in pages[0:i]:
                    return False
    return True 

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

        if part == Part.One:
            if update_ok(pages, rules):
                print(f"OK! {pages} {len(pages)/2} => {pages[ int(len(pages)/2)]}")
                num += pages[ int(len(pages)/2)]
        else:
            if not update_ok(pages, rules):
                corrected = sorted(pages, key=cmp_to_key(compare_to_rules))
                #print(f"FIXED! {pages} => {corrected} {len(pages)/2} => {corrected[ int(len(pages)/2)]}")
                num += corrected[ int(len(corrected)/2)]

#                perms = permutations(pages)
#                for perm in perms:
#                    if update_ok(perm, rules):
#                        print(f"FIXED! {pages} => {perm} {len(pages)/2} => {perm[ int(len(pages)/2)]}")
#                        num += perm[ int(len(pages)/2)]
#                        break

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
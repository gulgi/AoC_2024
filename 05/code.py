from enum import Enum
import sys
import re

class Part(Enum):
    One = 1,
    Two = 2

def read_rules(file):
    rules = {}
    while True:
        data = file.readline()
        if len(data) < 2:
            #print(f"rules: {rules}")
            return rules
        data = data.split("|")
        key = int(data[0])
        value = int(data[1].strip())
        if key not in rules:
            rules[key] = [value]
        else:
            rules[key].append(value)

def update_ok(pages, rules):
    print(f"pages {pages}")
    for i in range(0, len(pages)):
        page = pages[i]
        if page in rules:
            for rule in rules[page]:
                for j in range(0, i):
                    if rule < pages[j]:
                        print(f"page {page} rule {rule}  {pages[j]}")
                        return False
    return True 

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False

    # Read in file
    file = open("test.txt" if test else "input.txt")
    rules = read_rules(file)

    lines = file.readlines()

    # CODE
    num = 0
    if part == Part.One:
        for line in lines:
            #print(f"line: {line}")
            pages = list(map(int, line.strip().split(',')))

            if update_ok(pages, rules):
                print(f"OK! {pages} {(len(pages)+1)/2}")
                num += pages[ int((len(pages)+1)/2)]

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
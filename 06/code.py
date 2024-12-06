from enum import Enum
import sys
from functools import cmp_to_key

class Part(Enum):
    One = 1,
    Two = 2

def guard_init(data):
    pos = (1,1)
    dir = (0,-1)
    return pos, dir

def guard_move(data, guard_pos, guard_dir):
    return guard_pos, True

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    data = file.read().split()

    guard_pos, guard_dir = guard_init(data)

    # CODE
    num = 0
    positions = set()
    if part == Part.One:
        while True:
            guard_pos, inside = guard_move(data, guard_pos, guard_dir)
            if not inside:
                num = len(positions)
                break
            positions.add(guard_pos)

    # Output
    if test:
        print("Part: ", part, " Test: ", test, " correct: ", num == 41)
    else:
        print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
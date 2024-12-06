from enum import Enum
import sys
from functools import cmp_to_key

class Part(Enum):
    One = 1,
    Two = 2

def guard_init(data):
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            c = data[y][x]
            if c in '<>^v':
                pos = (y,x)
                match c:
                    case '<':
                        dir = (0, -1)
                    case '>':
                        dir = (0, 1)
                    case '^':
                        dir = (-1, 0)
                    case 'v':
                        dir = (1, 0)
                break
    print(f"Init pos {pos}, dir {dir}")
    return pos, dir

def new_dir(old_dir):
    match old_dir:
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)

def guard_move(data, guard_pos, guard_dir):
    new_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
    inside = False if new_pos[1] < 0 or new_pos[1] >= len(data[0]) or new_pos[0] < 0 or new_pos[0] >= len(data) else True

    if inside:
        if data[new_pos[0]][new_pos[1]] == '#':
            guard_dir = new_dir(guard_dir)
#            print(f"Turn pos {guard_pos}, dir {guard_dir}")
        else:
            guard_pos = new_pos
    else:
        guard_pos = new_pos

#    print(f"New pos {guard_pos}, dir {guard_dir} inside {inside}")
    return guard_pos, guard_dir, inside

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
    positions.add(guard_pos)

    if part == Part.One:
        while True:
            guard_pos, guard_dir, inside = guard_move(data, guard_pos, guard_dir)
            if not inside:
                num = len(positions)
                break
            positions.add(guard_pos)
    else:
        print("Not done yet :P")

    # Output
    if test:
        print("Part: ", part, " Test: ", test, " correct: ", num == 41)
    else:
        print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

# 5305
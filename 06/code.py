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
    #print(f"Init pos {pos}, dir {dir}")
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

def guard_move(data, guard_pos, guard_dir, dir_set):
    new_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
    inside = False if new_pos[1] < 0 or new_pos[1] >= len(data[0]) or new_pos[0] < 0 or new_pos[0] >= len(data) else True
    loop = False

    if inside:
        if data[new_pos[0]][new_pos[1]] == '#':
            guard_dir = new_dir(guard_dir)
            dir = (new_pos[0], new_pos[1], guard_dir[0], guard_dir[1])
            if dir in dir_set:
                loop = True
            dir_set.add(dir)
        else:
            guard_pos = new_pos
    else:
        guard_pos = new_pos

#    print(f"New pos {guard_pos}, dir {guard_dir} inside {inside}")
    return guard_pos, guard_dir, inside, loop

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
    dir_set = set()

    if part == Part.One:
        while True:
            guard_pos, guard_dir, inside, loop = guard_move(data, guard_pos, guard_dir, dir_set)
            if not inside:
                num = len(positions)
                break
            positions.add(guard_pos)
    else:
        loops = 0
        blocking_positions = set()
        while True:
            mod_guard_pos, mod_guard_dir, mod_inside, loop = guard_move(data, guard_pos, guard_dir, dir_set)
            if mod_guard_dir == guard_dir and mod_inside and mod_guard_pos not in blocking_positions and mod_guard_pos not in positions:
                mod_data = data.copy()
                mod_dir_set = dir_set.copy()
                mod_data[mod_guard_pos[0]] = mod_data[mod_guard_pos[0]][:mod_guard_pos[1]] + '#' + mod_data[mod_guard_pos[0]][mod_guard_pos[1]+1:]
                blocking_pos = mod_guard_pos
                blocking_positions.add(blocking_pos)
                mod_guard_pos = guard_pos
                mod_guard_dir = guard_dir
                mod_inside = True
                while True:
                    mod_guard_pos, mod_guard_dir_new, mod_inside, loop = guard_move(mod_data, mod_guard_pos, mod_guard_dir, mod_dir_set)
                    if loop:
                        loops += 1
                        break
                    if not mod_inside:
                        break
                    mod_guard_dir = mod_guard_dir_new

            guard_pos, guard_dir, inside, loop = guard_move(data, guard_pos, guard_dir, dir_set)
            if not inside:
                break
            positions.add(guard_pos)
        num = loops
 
    # Output
    if test:
        print("Part: ", part, " Test: ", test, " correct: ", num == 41 if part == Part.One else num == 6)
    else:
        print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

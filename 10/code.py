from enum import Enum
import sys
import string

class Part(Enum):
    One = 1,
    Two = 2

def walk(x, y, map, visited, nines):
    if map[y][x] == '9':
        if (x, y) in nines:
            print(f"9!! .. again {x} {y}")
            return 0
        nines.add((x, y))
        print(f"9!! {x} {y}")
        return 1
    num = 0
#    visited = visited_orig.copy()

    width = len(map[0])-1
    height = len(map)-1

    visited.add((x, y))
    if (x-1, y) not in visited and x > 0 and (ord(map[y][x-1]) - ord(map[y][x])) == 1:
        num = num + walk(x-1, y, map, visited, nines)
    if (x+1, y) not in visited and x < width and (ord(map[y][x+1]) - ord(map[y][x])) == 1:
        num = num + walk(x+1, y, map, visited, nines)
    if (x, y-1) not in visited and y > 0 and (ord(map[y-1][x]) - ord(map[y][x])) == 1:
        num = num + walk(x, y-1, map, visited, nines)
    if (x, y+1) not in visited and y < height and (ord(map[y+1][x]) - ord(map[y][x])) == 1:
        num = num + walk(x, y+1, map, visited, nines)
    return num

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    trail_map = list(map(list, file.read().split('\n')))
    print(f"{trail_map}")

    # CODE
    num = 0
    if part == Part.One:
        for y in range(0, len(trail_map)):
            for x in range(0, len(trail_map[0])):
                if trail_map[y][x] == '0':
                    visited = set()
                    nines = set()
                    num = num + walk(x, y, trail_map, visited, nines)
    else:
        num = 2

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

# 9813645302006 too high
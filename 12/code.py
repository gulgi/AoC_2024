from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict

class Part(Enum):
    One = 1,
    Two = 2

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    data = file.read().split('\n')

    # CODE
    num = 0

    width = len(data[0])-1
    height = len(data)-1
    if part == Part.One:
        done = set()
        for y in range(0, height+1):
            for x in range(0, width+1):
                if (x,y) in done:
                    continue

                to_visit = []
                area = 0
                fence = 0
                letter = '_'                
                to_visit.append((x,y))
                letter = data[y][x]
                while len(to_visit) > 0:
                    x,y = to_visit.pop()
                    if (x,y) in done:
                        continue
                    done.add((x,y))
                    area += 1

                    if y == 0 or letter != data[y-1][x]:
                        fence += 1
                    elif y > 0 and letter == data[y-1][x]:
                        to_visit.append((x, y-1))

                    if x == 0 or letter != data[y][x-1]:
                        fence += 1
                    elif x > 0 and letter == data[y][x-1]:
                        to_visit.append((x-1, y))
                        
                    if y == height or letter != data[y+1][x]:
                        fence += 1
                    elif y < height and letter == data[y+1][x]:
                        to_visit.append((x, y+1))
                        
                    if x == width or letter != data[y][x+1]:
                        fence += 1
                    elif x < width and letter == data[y][x+1]:
                        to_visit.append((x+1, y))

                print(f"{letter} {area} * {fence} => {area*fence}")
                num += area * fence
    if part == Part.Two:
        fence = DefaultDict(lambda: 0)
        area = DefaultDict(lambda: 0)
        for y in range(0, height):
            for x in range(0, width):
                letter = data[y][x]
                area[letter] += 1
                if y == 0 or letter != data[y-1][x]:
                    fence[letter] += 1
                if x == 0 or letter != data[y][x-1]:
                    fence[letter] += 1
                if y == height or letter != data[y+1][x]:
                    fence[letter] += 1
                if x == width or letter != data[y][x+1]:
                    fence[letter] += 1
        total_area = sum(area.values())
        total_fence = sum(fence.values())
        num = total_area * total_fence

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

# too low  1477448
# too low  1477740

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

    width = len(data[0])
    height = len(data)

    done = set()
    for y_ in range(0, height):
        for x_ in range(0, width):
            if (x_,y_) in done:
                continue

            to_visit = []
            area = 0
            fence = 0
            letter = '_'                
            to_visit.append((x_,y_))
            letter = data[y_][x_]
            while len(to_visit) > 0:
                x,y = to_visit.pop()
                if (x,y) in done:
                    continue

                done.add((x,y))
                area += 1

                # up
                if y == 0:
                    fence += 1
                elif letter != data[y-1][x]:
                    fence += 1
                else: #if letter == data[y-1][x]:
                    to_visit.append((x, y-1))

                # left
                if x == 0:
                    fence += 1
                elif letter != data[y][x-1]:
                    fence += 1
                else: #if letter == data[y][x-1]:
                    to_visit.append((x-1, y))

                # down
                if y == height-1:
                    fence += 1
                elif letter != data[y+1][x]:
                    fence += 1
                else: #if letter == data[y+1][x]:
                    to_visit.append((x, y+1))

                # right                        
                if x == width-1:
                    fence += 1
                elif letter != data[y][x+1]:
                    fence += 1
                else: # if letter == data[y][x+1]:
                    to_visit.append((x+1, y))

            ##print(f"{letter} {area} * {fence} => {area*fence}")
            num += area * fence

#    print(f"done: {len(done)}  {width} x {height} => {height*width}")

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

# too low  1477448
# too low  1477740

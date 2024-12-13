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

            blocks = set()
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
                blocks.add((x,y))
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

            #blocks ...
            def num_edges():
                num = 0
                for y in range(0, height): # upper/lower edge
                    in_edge, in_edge2 = False, False
                    for x in range(0, width):
                        if (x,y) in blocks:
                            if y == 0 or (x,y-1) not in blocks:
                                in_edge = True
                            else:
                                if in_edge:
                                    num += 1
                                    in_edge = False

                            if y == height-1 or (x,y+1) not in blocks:
                                in_edge2 = True
                            else:
                                if in_edge2:
                                    num += 1
                                    in_edge2 = False
                        else:
                            if in_edge:
                                num += 1
                            if in_edge2:
                                num += 1
                            in_edge, in_edge2 = False, False
                    if in_edge:
                        num += 1
                    if in_edge2:
                        num += 1

                for x in range(0, width): # left/right edge
                    in_edge, in_edge2 = False, False
                    for y in range(0, height):
                        if (x,y) in blocks:
                            if x == 0 or (x-1,y) not in blocks:
                                in_edge = True
                            else:
                                if in_edge:
                                    num += 1
                                    in_edge = False
                            if x == width-1 or (x+1,y) not in blocks:
                                in_edge2 = True
                            else:
                                if in_edge2:
                                    num += 1
                                    in_edge2 = False
                        else:
                            if in_edge:
                                num += 1
                            if in_edge2:
                                num += 1
                            in_edge, in_edge2 = False, False
                    if in_edge:
                        num += 1
                    if in_edge2:
                        num += 1
                return num

            if part == Part.One:
                num += area * fence
            else:
                edges = num_edges()
#                print(f"{letter} => edges {edges}")
                num += area * edges

            ##print(f"{letter} {area} * {fence} => {area*fence}")

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

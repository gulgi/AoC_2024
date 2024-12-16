from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re
import numpy
from collections import OrderedDict

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
    data = file.read()

    data, inputs = data.split("\n\n")
    inputs = inputs.replace('\n', '')
    warehouse = list(map(list, data.split('\n')))

    # Modify data for part 2
    if part == Part.Two:
        w2 = warehouse
        index = 0
        for line in warehouse:
            line2 = []
            for thing in line:
                if thing == '#':
                    line2.append('#')
                    line2.append('#')
                elif thing == '@':
                    line2.append('@')
                    line2.append('.')
                elif thing == 'O':
                    line2.append('[')
                    line2.append(']')
                else:
                    line2.append('.')
                    line2.append('.')
            w2[index] = line2
            index += 1
        warehouse = w2

    print(f"warehouse {warehouse}")
    print(f"input {inputs}")

    def find_start():
        for y in range(1, len(warehouse)-1):
            for x in range(1, len(warehouse[0])-1):
                if warehouse[y][x] == '@':
                    warehouse[y][x] = '.'
                    return x,y
        return -1,-1
    pos = numpy.array(find_start())
    arrows = { '<': numpy.array([-1,0]), '>': numpy.array([1,0]),
              '^': numpy.array([0,-1]), 'v': numpy.array([0,1]), }

    # CODE
    num = 0
    for input in inputs:
        dir = arrows[input]
        pos2 = numpy.add(pos, dir)

        def new_pos_func(new_pos, dir):
            dir_y = dir[1]
            x = new_pos[0]
            y = new_pos[1]
            at_pos = warehouse[y][x]
            if at_pos == '#':
                return False
            if at_pos == '.':
                return True
            else:
                if dir[1] == 0:
                    empty_pos = new_pos
                    while True:
                        empty_pos = numpy.add(empty_pos, dir)
                        empty_x,empty_y = empty_pos
                        at_pos = warehouse[empty_y][empty_x]
                        if at_pos == '#':
                            return False
                        if at_pos == '.':
                            for x_ in range(empty_x, x, -dir[0]):
                                warehouse[y][x_] = warehouse[y][x_-dir[0]]
                            warehouse[y][x] = '.'
                            return True
                else:
                    print(f"up/down  {new_pos}")
#                    points_to_check = [ numpy.add(new_pos, dir) ]
                    points_to_move = []
                    points_to_check = [ new_pos ]
                    while len(points_to_check) > 0:
                        check_pos = points_to_check.pop()
                        check_x,check_y = check_pos
                        at_check_pos = warehouse[check_y][check_x]

                        print(f"at_check_pos {at_check_pos}")

                        if at_check_pos == 'O':
                            points_to_check.append(numpy.array([check_x, check_y+dir_y]))
                            move_p = (check_x, check_y)
                            points_to_move.append(move_p)
                            print(f"O adding {check_pos}")
                        elif at_check_pos == '[':
                            points_to_check.append(numpy.array([check_x, check_y+dir_y]))
                            points_to_check.append(numpy.array([check_x+1, check_y+dir_y]))
                            move_p = (check_x, check_y)
                            if move_p not in set(points_to_move):
                                points_to_move.append(move_p)
                            print(f"[ adding {move_p}")
                        elif at_check_pos == ']':
                            points_to_check.append(numpy.array([check_x, check_y+dir_y]))
                            points_to_check.append(numpy.array([check_x-1, check_y+dir_y]))
                            move_p = (check_x-1, check_y)
                            if move_p not in set(points_to_move):
                                points_to_move.append(move_p)
                            #print(f"] adding {numpy.array([check_x-1, check_y])}")

                        if at_check_pos == '#':
                            print(f" > #")
                            return False
                    # Done
                    print(f"To Move: {points_to_move}")
                    if len(points_to_move) > 0:
                        for point in reversed(points_to_move):
                            x,y = point
                            at = warehouse[y][x]
                            warehouse[y+dir_y][x] = warehouse[y][x]
                            warehouse[y][x] = '.'
                            if at != 'O':
                                warehouse[y+dir_y][x+1] = warehouse[y][x+1]
                                warehouse[y][x+1] = '.'

                        return True
                    return False

        if new_pos_func(pos2, dir):
            pos = pos2

    # sum boxes
    for y in range(1, len(warehouse)):
        for x in range(1, len(warehouse[0])):
            if warehouse[y][x] == 'O' or warehouse[y][x] == '[':
                num += y*100 + x

    for x in warehouse:
        print(f"{x}")

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

##  1510330  too low

## Test works. Dammit.
##  What edge case goes bad? :/ 

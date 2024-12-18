from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re
import numpy
from collections import OrderedDict
import time

class Part(Enum):
    One = 1,
    Two = 2

dirs = { 0: numpy.array([-1,0]), 1: numpy.array([0,-1]), 2: numpy.array([1,0]), 3: numpy.array([0,1]) }

best_score = 100000000
width = 6

def walk(data, visited, pos, dir, score, score_board):
    global width
    global best_score

    if pos[0] < 0 or pos[0] > width:
        return 100000000
    if pos[1] < 0 or pos[1] > width:
        return 100000000

    pos_ = (pos[0], pos[1])
    at = data[pos[1]][pos[0]]
    if pos_ in score_board:
        if score > score_board[pos_]:
            return 100000000
    score_board[pos_] = score

    if pos_ in visited or at == 1:
        return 100000000
    if score > best_score:
        return 100000000
    if at == 2:
        if score < best_score:
            print(f"SCORE {score}  BEST")
            best_score = score
        else:
            print(f"SCORE {score}")
        return score

    visited.add( pos_ )
    new_visited = visited.copy()

    # first try in same direction
    new_pos0 = numpy.add(pos, dirs[dir])
    num0 = walk(data, new_visited, new_pos0, dir, score + 1, score_board)
    new_pos1 = numpy.add(pos, dirs[(dir+1)%4])
    num1 = walk(data, new_visited, new_pos1, (dir+1)%4, score + 1, score_board)
    new_pos2 = numpy.add(pos, dirs[(dir+3)%4])
    num2 = walk(data, new_visited, new_pos2, (dir+3)%4, score + 1, score_board)

    return min(min(num0, num1), num2)

def main():
    global width

    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    width = 6 if test else 70 # inclusive
    start = numpy.array([0,0])
    end = numpy.array([width,width])

    # Read in file
    file = open(file_name)
    data = file.read().split("\n")
    coords = []
    for line in data:
        coords.append((list(map(int, line.split(",")))))

    data = [[0 for x in range(width+1)] for y in range(width+1)] 
    simulate = 12 if test else 1024
    for i in range(0, simulate):
        coord = coords[i]
        data[coord[1]][coord[0]] = 1
    data[end[1]][end[0]] = 2

    # CODE
    sys.setrecursionlimit(3500)  # Yay! :P   This much is not needed, but ....

    dir = 2
    visited = set()
    score_board = {}
    num = walk(data, visited, start, dir, 0, score_board)

#    for line in data:
#        print(f"{line}")

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

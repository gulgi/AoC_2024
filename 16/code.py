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

dirs = { 0: numpy.array([-1,0]), 1: numpy.array([0,-1]), 2: numpy.array([1,0]), 3: numpy.array([0,1]) }
arrows = { 0: '<', 1: '^', 2: '>', 3: 'v' }

best_score = 100000000000

best_path = set()
best_path_score = 4009 # 11048

def walk(data, visited, pos, dir, score, score_board):
    global best_score
    global best_path 
    pos_ = (pos[0], pos[1])
    at = data[pos[1]][pos[0]]
#    if at != '#':
#        print(f"depth {depth}  at {pos} => {at}")
    if pos_ in score_board:
        if score > score_board[pos_]:
            return 100000000
    score_board[pos_] = score

    if pos_ in visited or at == '#':
        return 100000000
    if score > best_score:
#        print(f"More expensive .. {score} > {best_score}")
        return 100000000
    if at == 'E':
        if score < best_score:
            print(f"SCORE {score}  BEST")
            best_score = score
        else:
            print(f"SCORE {score}")
        if score == best_path_score:
            best_path.add(pos_)
        return score

    visited.add( pos_ )
    new_visited = visited.copy()

    # first try in same direction
    new_pos0 = numpy.add(pos, dirs[dir])
    num0 = walk(data, new_visited, new_pos0, dir, score + 1, score_board)
    if num0 == best_path_score:
        best_path.add((new_pos0[0], new_pos0[1]))
    new_pos1 = numpy.add(pos, dirs[(dir+1)%4])
    num1 = walk(data, new_visited, new_pos1, (dir+1)%4, score + 1001, score_board)
    if num1 == best_path_score:
        best_path.add((new_pos1[0], new_pos1[1]))
    new_pos2 = numpy.add(pos, dirs[(dir+3)%4])
    num2 = walk(data, new_visited, new_pos2, (dir+3)%4, score + 1001, score_board)
    if num2 == best_path_score:
        best_path.add((new_pos2[0], new_pos2[1]))

    return min(min(num0, num1), num2)

def main():
    global best_path 

    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    if not test:
        best_path_score = 134588

    # Read in file
    file = open(file_name)
    data = file.read().split('\n')
#    data = data.split("\n")

    def find_pos(c):
        for y in range(1, len(data)-1):
            for x in range(1, len(data[0])-1):
                if data[y][x] == c:
                    return numpy.array([x,y])
        return numpy.array([-1,-1])
    pos = find_pos('S')
    end = find_pos('E')
    dir = 2
    visited = set()
    print(f"S {pos}")
    print(f"E {end}")

    # CODE

    sys.setrecursionlimit(3500)

    score_board = {}
    best_path.add((pos[0], pos[1]))
    num = walk(data, visited, pos, dir, 0, score_board)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)
    print("Best Path: ", len(best_path))

#    for path in best_path:
#        data[path[1]] = data[path[1]][:path[0]] + 'O' + data[path[1]][path[0]+1:]
#    for x in data:
#        print(f"{x}")

if __name__=="__main__":
    main()

##  1510330  too low

## Test works. Dammit.
##  What edge case goes bad? :/ 

from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re
import numpy
from collections import OrderedDict
import time
import networkx as nx

class Part(Enum):
    One = 1,
    Two = 2

dirs = { 0: numpy.array([-1,0]), 1: numpy.array([0,-1]), 2: numpy.array([1,0]), 3: numpy.array([0,1]) }

width = 6

def main():
    global width

    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    width = 6 if test else 70 # inclusive
    start = (0,0)
    end = (width,width)

    # Read in file
    file = open(file_name)
    data = file.read().split("\n")
    coords = []
    for line in data:
        coords.append((list(map(int, line.split(",")))))

    simulate = 12 if test else 1024

    def func(simulate):
        data = [[0 for x in range(width+1)] for y in range(width+1)] 
        for i in range(0, simulate):
            coord = coords[i]
            data[coord[1]][coord[0]] = 1

        G = nx.Graph()

        for y in range(0, width+1):
            for x in range(0, width+1):
                if data[y][x] == 0:
                    pos = (x, y)
                    G.add_node(pos)
                    if y > 0 and data[y-1][x] == 0:
                        G.add_edge(pos, (x, y-1))
                    if x > 0 and data[y][x-1] == 0:
                        G.add_edge(pos, (x-1, y))
                    if y < width and data[y+1][x] == 0:
                        G.add_edge(pos, (x, y+1))
                    if x < width and data[y][x+1] == 0:
                        G.add_edge(pos, (x+1, y))
        try:
            return nx.shortest_path_length(G, start, end)
        except:
            return -1

    if part == Part.One:
        result = func(simulate)
    else:
        for extra in range(len(coords)-simulate):
            result = func(simulate+extra)
            if result < 0:
                print(f"Breaking coord: {coords[simulate+extra-1]}")
                result = coords[simulate+extra-1]
                break

    # Output
    print("Part: ", part, " Test: ", test)
    print("Result: ", result)

if __name__=="__main__":
    main()

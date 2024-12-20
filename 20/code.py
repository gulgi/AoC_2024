from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re
import numpy
from collections import OrderedDict
import time
import networkx as nx
from functools import cache

class Part(Enum):
    One = 1,
    Two = 2

@cache
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
#    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    # Read in file
    file = open(file_name)
    data = list(map(list, file.read().split('\n')))

    def find_pos(c):
        for y in range(1, len(data)-1):
            for x in range(1, len(data[0])-1):
                if data[y][x] == c:
                    return (x,y)
        return (-1,-1)
    start = find_pos('S')
    end = find_pos('E')

    data[start[1]][start[0]] = '.'
    data[end[1]][end[0]] = '.'

    path_lenghts = DefaultDict(lambda: 0)
    width = len(data[0])
    height = len(data)

    def func1():
        print(f"{start} => {end}")
        map = data.copy()
        G = nx.Graph()
        already_tried = set()
        for y in range(0, len(map)):
            for x in range(0, len(map[0])):
                if map[y][x] == '.':
                    pos = (x, y)
                    G.add_node(pos)
                    already_tried.add(pos)
                    if map[y-1][x] == '.':
                        G.add_edge(pos, (x, y-1))
                    if map[y][x-1] == '.':
                        G.add_edge(pos, (x-1, y))
                    if map[y+1][x] == '.':
                        G.add_edge(pos, (x, y+1))
                    if map[y][x+1] == '.':
                        G.add_edge(pos, (x+1, y))
        shortest_path = nx.shortest_path(G, start, end)
        shortest_path_len = nx.shortest_path_length(G, start, end)

        def add_extra_point(x, y, Graph):
            if x < 1 or x >= width-1 or y < 1 or y >= height-1:
                return False, None

            pos = (x,y)
            if pos in already_tried:
                return False, None
            if map[y][x] != '#':
                return False, None
            already_tried.add(pos)

            edges = []
            if map[y-1][x] == '.':
                edges.append((x, y-1))
            if map[y][x-1] == '.':
                edges.append((x-1, y))
            if map[y+1][x] == '.':
                edges.append((x, y+1))
            if map[y][x+1] == '.':
                edges.append((x+1, y))

            if len(edges) == 0:
                return False, None

            G_ = Graph.copy()
            G_.add_node(pos)
            for edge in edges:
                G_.add_edge(pos, edge)
            return True, G_

        for point in tqdm(shortest_path):
            x,y = point
            do, G2 = add_extra_point(x-1, y, G)
            if do:
                path_lenghts[nx.shortest_path_length(G2, start, end)] += 1
            do, G2 = add_extra_point(x+1, y, G)
            if do:
                path_lenghts[nx.shortest_path_length(G2, start, end)] += 1
            do, G2 = add_extra_point(x, y-1, G)
            if do:
                path_lenghts[nx.shortest_path_length(G2, start, end)] += 1
            do, G2 = add_extra_point(x, y+1, G)
            if do:
                path_lenghts[nx.shortest_path_length(G2, start, end)] += 1
        return shortest_path_len

    def func2():
        map = data.copy()
        G = nx.Graph()
        for y in range(0, len(map)):
            for x in range(0, len(map[0])):
                if map[y][x] == '.':
                    pos = (x, y)
                    G.add_node(pos)
                    if map[y-1][x] == '.':
                        G.add_edge(pos, (x, y-1), length=1)
                    if map[y][x-1] == '.':
                        G.add_edge(pos, (x-1, y), length=1)
                    if map[y+1][x] == '.':
                        G.add_edge(pos, (x, y+1), length=1)
                    if map[y][x+1] == '.':
                        G.add_edge(pos, (x+1, y), length=1)
        shortest_path = nx.shortest_path(G, start, end)        
        shortest_path_len = len(shortest_path)

        for point_index in tqdm(range(len(shortest_path[:-10]))):
            point = shortest_path[point_index]

            for point2_index in range(shortest_path_len-1, point_index+10, -1):
                point2 = shortest_path[point2_index]
                dist = manhattan(point, point2)
                if dist <= 20:
                    path_lenghts[point_index + dist + (shortest_path_len-point2_index)] += 1
            #break

        return shortest_path_len

    num = 0
    if part == Part.One:
        shortest_path = func1()
        for item in path_lenghts.items():
            num_item, count = item
            if shortest_path - num_item >= 100:
                num += count
    else:
        shortest_path = func2()
        cutoff = 50 if test else 100
        for item in path_lenghts.items():
            num_item, count = item
            if shortest_path - num_item >= cutoff:
                num += count
                if test:
                    print(f"{count} that saves {shortest_path-num_item}")

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

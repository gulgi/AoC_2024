from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re
import numpy
from collections import OrderedDict
import time
import networkx as nx
import itertools

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

    # Read in file
    file = open(file_name)
    towels,data = file.read().split("\n\n")
    towels = towels.split(", ")
    designs = data.split("\n")

    towels.sort(key=lambda s: len(s), reverse=True)
    #print(f"towels {towels}")
    #print(f"designs {designs}")
    towel_permutations = set(itertools.permutations(towels))
    print(f"towels {towels}")
    print(f"towel_permutations {towel_permutations}")

    def func(design):
#        G = nx.Graph()
#        print(f"design: {design} BEFORE")
        for towel_permutation in towel_permutations:
            design_try = design
            for towel in towel_permutation:
                design_try = design_try.replace(towel, " ")
#        print(f"design: {design} AFTER")
            design_try = design_try.strip()
            if len(design_try) == 0:
                return True
        return False
    
    num = 0
    if part == Part.One:
        for design in designs:
            if func(design):
                num += 1

    # Output
    print("Part: ", part, " Test: ", test)
    print("Result: ", num)

if __name__=="__main__":
    main()

# 75 just straight on. Too low, obviusly. Had to try.
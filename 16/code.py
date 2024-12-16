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
    data = file.read().split('\n')
#    data = data.split("\n")

    def find_start():
        for y in range(1, len(data)-1):
            for x in range(1, len(data[0])-1):
                if data[y][x] == 'S':
                    return x,y
        return -1,-1
    pos = find_start()

    # CODE
    num = 0
    for x in data:
        print(f"{x}")

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

##  1510330  too low

## Test works. Dammit.
##  What edge case goes bad? :/ 

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

def prune(num):
    return num & 0xffffff

def mix(secret, num):
    return secret ^ num

def evolve_secret(secret):
    num = secret * 64
    secret = mix(secret, num)
    secret = prune(secret)

    num = secret // 32
    secret = mix(secret, num)
    secret = prune(secret)

    num = secret * 2048
    secret = mix(secret, num)
    secret = prune(secret)

    return secret


def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    data = list(map(int, file.read().split('\n')))

    num = 0

    for initial_secret in data:
        secret = initial_secret
#        print(f"{secret} => ", end="")
        for i in range(2000):
            secret = evolve_secret(secret)
#        print(secret)
        num += secret

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

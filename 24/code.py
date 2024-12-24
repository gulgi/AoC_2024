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

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    init,data = file.read().split('\n\n')
    init = init.split("\n")
    data = data.split("\n")

    gates = []

    ready = {}

    for i in init:
        gate = {}
        name, on = i.split(": ")
        gate["signal"] = bool(int(on))
        gate["out"] = name
        gate["ready"] = True

        ready[name] = bool(int(on)) # actually use this...

        #gates.append(gate)

#    print(f"{ready}")

    for d in data:
        in0, op, in1, out = re.match("(\w+) (\w+) (\w+) -> (\w+)", d).groups()
#        print(f"{in0} {op} {in1} {out}")

        gate = {}
        gate["in0"] = in0
        gate["in1"] = in1
        gate["op"] = op
        gate["out"] = out
        gate["ready"] = False

        gates.append(gate)

    while True:
        done = True
        for gate in gates:
#            print(f"gate {gate}")
            if gate["ready"] == True:
                continue
            done = False

            in0 = gate["in0"]
            in1 = gate["in1"]
#            print(f"in0 {in0}  in1 {in1}  ready {ready}")
            if in0 in ready and in1 in ready:
                out = 0
                if gate["op"] == "AND":
                    out = ready[in0] & ready[in1]
                elif gate["op"] == "OR":
                    out = ready[in0] | ready[in1]
                else: # gate["op"] == "XOR":
                    out = ready[in0] ^ ready[in1]
                gate["ready"] = True
                ready[gate["out"]] = out

        if done:
            break

    num = 0
    for r in ready:
        if r.startswith("z"):
            print(f"{r}")
            d = int(r[1:])
            if ready[r]:
                num += 1 << d 

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

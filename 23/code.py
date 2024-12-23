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
import string

class Part(Enum):
    One = 1,
    Two = 2

def manhattan(a : int, b : int) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    data = list(map(lambda x : x.split("-"), file.read().split('\n')))

    nodes = {}
    node_set = set()
    for d in data:
        node_set.add(d[0])
        node_set.add(d[1])
        nodes.setdefault(d[0], []).append(d[1])
        nodes.setdefault(d[1], []).append(d[0])

    tris = set()
    num = 0
    for key in nodes.keys():
        for connection1 in nodes[key]:
            for connection2 in nodes[connection1]:
                if key in nodes[connection2]:
                    keys = [key,connection1,connection2]
                    keys = list(sorted(keys))
#                    new_tri = tuple(set([key,connection1,connection2]))
                    new_tri = tuple(set(keys))
                    tris.add(new_tri)

    for tri in tris:
        a,b,c = tri
        if a[0] == 't' or b[0] == 't' or c[0] == 't':
            print(tri)
            num += 1

    '''
    G = nx.graph.Graph()
    for node in nodes:
        G.add_node(node)
    for d in data:
        G.add_edge(d[0],d[1])

    num = 0
    exceptions = 0
    for c in string.ascii_lowercase:
        starts_with_t = "t" + c
        n = nx.node_connected_component(G, starts_with_t)
        n = nx.all_pairs_node_connectivity(G, starts_with_t)
        print(f"{starts_with_t}  {n}")
        if n == 2:
            num += 1
#        except:
#            # This is fine
#            exceptions += 1
    '''

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

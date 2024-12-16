from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict
import re
import numpy
import time

class Part(Enum):
    One = 1,
    Two = 2

def is_possibly_tree(robots):
    possibly_a_tree = False
#    for y in range(0, 103):
    for y in range(30, 70):
        many = False
        last_found = False
#        for x in range(0, 101):
        for x in range(30, 70):
            found = False
            for robot in robots:
                if robot[0][0] == x and robot[0][1] == y:
                    found = True
                    break
            if found and last_found:
                many += 1
                if many >= 10:
                    if possibly_a_tree:
                        return True
                    possibly_a_tree = True
            if not found:
                many = 0
            last_found = found
    return False

def visualize(robots, number):
    f = open(f"tree_{number}.txt", "w")
    for y in range(0, 103):
        many = False
        for x in range(0, 101):
            found = False
            for robot in robots:
                if robot[0][0] == x and robot[0][1] == y:
                    found = True
                    break
            if found:
                f.write("x")
#                print("x", end="")
            else:
                f.write(" ")
#                print(" ", end="")
        f.write("\n")
#        print("")
    f.close()
    return False

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    robots = []
    # Read in file
    with open(file_name) as f:
        for line in f:
            px, py, vx, vy = list(map(int, re.match("p=(\d+),(\d+) v=([-]?\d+),([-]?\d+)", line).groups()))
            robots.append([numpy.array([px,py]), numpy.array([vx,vy])])
    
    # CODE
    num = 0
    seconds = 100 if part == Part.One else 10000
    width = 11 if test else 101
    height = 7 if test else 103
    for second in tqdm(range(0, seconds)):
        for robot in robots:
            robot[0] = numpy.add(robot[0], robot[1])
            while robot[0][0] < 0:
                robot[0][0] = robot[0][0] + width
            while robot[0][0] >= width:
                robot[0][0] = robot[0][0] - width
            while robot[0][1] < 0:
                robot[0][1] = robot[0][1] + height
            while robot[0][1] >= height:
                robot[0][1] = robot[0][1] - height

        if part == Part.Two:
            if is_possibly_tree(robots):
                visualize(robots, second+1)
                print(f"\nPossible after {second+1}")
#            time.sleep(0.5)
#            print(f"  NUM: {second}")

    # count quadrants
    quad0 = 0
    quad1 = 0
    quad2 = 0
    quad3 = 0
    for robot in robots:
        if robot[0][0] < width // 2:
            if robot[0][1] < height // 2:
                quad0 += 1
            elif robot[0][1] >= height - height // 2:
                quad1 += 1
        elif robot[0][0] >= width - width // 2:
            if robot[0][1] < height // 2:
                quad2 += 1
            elif robot[0][1] >= height - height // 2:
                quad3 += 1

    num = quad0*quad1*quad2*quad3

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

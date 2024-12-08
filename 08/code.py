from enum import Enum
import sys
import string

class Part(Enum):
    One = 1,
    Two = 2

def new_pos(width, height, node_i, node_j, part2):
    ret = []
    i_x = node_i[0]
    i_y = node_i[1]
    j_x = node_j[0]
    j_y = node_j[1]

    if part2:
        ret.append((i_x, i_y))
        ret.append((j_x, j_y))

    x_diff = i_x - j_x
    y_diff = i_y - j_y
    p0_x = i_x
    p0_y = i_y
    while True:
        p0_x = p0_x + x_diff
        p0_y = p0_y + y_diff
        if p0_x < 0 or p0_y < 0 or p0_x >= width or p0_y >= height:
            break
        ret.append((p0_x, p0_y))
        if not part2:
            break

    x_diff = j_x - i_x
    y_diff = j_y - i_y
    p0_x = j_x
    p0_y = j_y
    while True:
        p0_x = p0_x + x_diff
        p0_y = p0_y + y_diff
        if p0_x < 0 or p0_y < 0 or p0_x >= width or p0_y >= height:
            break
        ret.append((p0_x, p0_y))
        if not part2:
            break

    return ret

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    data = file.read().split('\n')

    width = len(data[0])
    height = len(data)

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    nodes = {}
    for c in characters:
        y = 0
        for line in data:
            x = line.find(c)
            if x >= 0:
                pos = (x, y)
                nodes.setdefault(c, []).append(pos)
            y = y + 1

    # CODE
    antinodes = set()
    num = 0
    for key in nodes.keys():
        size = len(nodes[key])
        for i in range(0, size-1):
            node_i = nodes[key][i]
            i_x = node_i[0]
            i_y = node_i[1]
            for j in range(i+1, size):
                node_j = nodes[key][j]

                points = new_pos(width, height, node_i, node_j, part == Part.Two)
                for point in points:
#                    print(f"point {point}")
                    antinodes.add(point)

    num = len(antinodes)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()
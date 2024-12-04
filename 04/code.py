from enum import Enum
import sys
import re

class Part(Enum):
    One = 1,
    Two = 2

def fix_input_1(file_name):
    file = open(file_name)
    lines = file.read().split()

    width = len(lines[0])
    height = len(lines)

    horizontal_lines = []
    for i in range(0, len(lines[0])):
        line = ""
        for j in range(0, len(lines)):
            line += lines[j][i]
        horizontal_lines.append(line)
    
    diag1_lines = []
    for y in range(0, len(lines)-3):
        line = ""
        for x in range(0, len(lines[0])):
            if (x+y) >= len(lines):
                break
            line += lines[y+x][x]
        diag1_lines.append(line)
        #print(f"DIAG: ", line)
    for x in range(1, len(lines[0])):
        line = ""
        for y in range(0, len(lines[0])):
            if (x+y) >= len(lines[0]):
                break
            line += lines[y][x+y]
        diag1_lines.append(line)
        #print(f"DIAG: ", line)

    diag2_lines = []
    for y in range(0, height-3):
        line = ""
        for x in range(0, width):
            if (x+y) >= height:
                break
            line += lines[y+x][width - x - 1]
        diag2_lines.append(line)
    for x in range(1, len(lines[0])):
        line = ""
        for y in range(0, len(lines[0])):
            if (x+y) >= height:
                break
            line += lines[y][width - x - 1 - y]
        diag2_lines.append(line)

    lines += horizontal_lines
    lines += diag1_lines
    lines += diag2_lines
    return lines

def fix_input_2(file_name):
    file = open(file_name)
    lines = file.read().split()
    return lines

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    num = 0
    if part == Part.One:
        # Read in file
        lines = fix_input_1(file_name)

        # CODE
        match_string1 = "XMAS"
        match_string2 = "SAMX"
        for line in lines:
            all1 = re.findall(match_string1, line)
            all2 = re.findall(match_string2, line)
            num += len(all1) + len(all2)
    else:
        lines = fix_input_2(file_name)

        # CODE #2
        width = len(lines[0])
        height = len(lines)
        for y in range(1, height-1):
            for x in range(1, width-1):
                if lines[y][x] == 'A':
                    xy0 = lines[y-1][x-1]
                    xy1 = lines[y+1][x+1]
                    xy2 = lines[y-1][x+1]
                    xy3 = lines[y+1][x-1]
                    if ((xy0 == 'M' and xy1 == 'S') or (xy0 == 'S' and xy1 == 'M')) and ((xy2 == 'M' and xy3 == 'S') or (xy2 == 'S' and xy3 == 'M')):
                        num += 1

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

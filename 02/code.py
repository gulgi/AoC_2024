from enum import Enum
import sys

class Part(Enum):
    One = 1,
    Two = 2

def is_data_safe(data):
    diff = data[0] - data[1]
    valid = [1, 2, 3] if diff > 0 else [-1, -2, -3]
    for i in range(1, len(data)):
        diff = data[i-1] - data[i]
        if diff not in valid:
            return False, i-1
    return True, -1

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # CODE
    with open(file_name) as f:
        num = 0
        for line in f:
            data = list(map(int, line.split()))
            is_ok, bad_index = is_data_safe(data)

            if part == Part.Two and is_ok == False:
                indices = list(set([0, bad_index, bad_index + 1]))
                for index in indices:
                    data0 = data.copy()
                    del data0[index]
                    is_ok, bad_index = is_data_safe(data0)
                    if is_ok == True:
                        break
            
            if is_ok == True:
                num += 1
        
    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()    
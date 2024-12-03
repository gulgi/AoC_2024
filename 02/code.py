from enum import Enum
import sys

class Part(Enum):
    One = 1,
    Two = 2

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False

    # CODE
    num = 0
    with open("test.txt" if test else "input.txt") as file:
        for line in file:
            numbers = list(map(int, line.split()))
            diff = numbers[0] - numbers[1]
            bad_index = -1
            if diff > 0 and diff <= 3:
                for i in range(1, len(numbers)):
                    diff = numbers[i-1] - numbers[i]
                    if diff <= 0 or diff > 3:
                        bad_index = i
                        break
                if bad_index != -1 and part == Part.Two:
                    del numbers[bad_index]
                    bad_index = -1
                    for i in range(1, len(numbers)):
                        diff = numbers[i-1] - numbers[i]
                        if diff <= 0 or diff > 3:
                            bad_index = i
                            break
            elif diff < 0 and diff >= -3:
                for i in range(1, len(numbers)):
                    diff = numbers[i-1] - numbers[i]
                    if diff >= 0 or diff < -3:
                        bad_index = i
                        break
                if bad_index != -1 and part == Part.Two:
                    del numbers[bad_index]
                    bad_index = -1
                    for i in range(1, len(numbers)):
                        diff = numbers[i-1] - numbers[i]
                        if diff >= 0 or diff < -3:
                            bad_index = i
                            break
            elif diff == 0:
                bad_index = 1
            if bad_index == -1:
                num += 1

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()    
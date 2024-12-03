from enum import Enum
import sys

class Part(Enum):
    One = 1,
    Two = 2

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False

    # Read in file
    file = open("test.txt" if test else "input.txt")
    numbers = list(map(int, file.read().split()))
    even = numbers[0::2]
    odd = numbers[1::2]

    # CODE
    num = 0
    if part == Part.One:
        even.sort()
        odd.sort()
        for first, second in zip(even, odd):
            num += abs(first - second)
    else:
        for first, second in zip(even, odd):
            if first in odd:
                num += first * odd.count(first)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()    
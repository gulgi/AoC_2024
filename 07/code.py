from enum import Enum
import sys
from functools import cmp_to_key

class Part(Enum):
    One = 1,
    Two = 2

def sum(actual_sum, number, numbers, depth):
#    print(f"sum {depth}, len(numbers) {len(numbers)}  number {number}")
    if depth == len(numbers):
#        print(f"actual_sum {actual_sum}, number {number}")
        if actual_sum == number:
            return True
        return False

    sum_number = number + numbers[depth]
    if sum(actual_sum, sum_number, numbers, depth+1):
        return True
    
    prod_number = number * numbers[depth]
    return sum(actual_sum, prod_number, numbers, depth+1)

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    calibrations = file.read().split('\n')

    print(f"calibrations {calibrations}")

    # CODE
    num = 0
    blah = 0

    if part == Part.One:
        for cal in calibrations:
            actual_sum, numbers = cal.split(': ')
            actual_sum = int(actual_sum)
            numbers = numbers.split(' ')
            numbers = list(map(int, numbers))

            number = numbers[0]
            sum_ok = sum(actual_sum, number, numbers, 1)
            if sum_ok:
                print(f"sum_ok {actual_sum} {numbers}")
                num = num + actual_sum

    # Output
    if test:
        print("Part: ", part, " Test: ", test, " correct: ", num == 3749 if part == Part.One else num == 6)
    else:
        print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

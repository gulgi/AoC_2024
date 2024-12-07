from enum import Enum
import sys

class Part(Enum):
    One = 1,
    Two = 2

def sum(concat, actual_sum, number, numbers, depth):
    if depth == -1:
        if actual_sum == number:
            return True
        return False

    sum_number = number + numbers[depth]
    if sum(concat, actual_sum, sum_number, numbers, depth-1):
        return True
    
    prod_number = number * numbers[depth]
    if sum(concat, actual_sum, prod_number, numbers, depth-1):
        return True
    if concat:
        prod_number = int(str(number) + str(numbers[depth]))
        return sum(concat, actual_sum, prod_number, numbers, depth-1)
    return False

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    calibrations = file.read().split('\n')

    # CODE
    num = 0
    for cal in calibrations:
        actual_sum, numbers = cal.split(': ')
        actual_sum = int(actual_sum)
        numbers = numbers.split(' ')
        numbers = list(map(int, numbers))

        number = numbers[0]
        numbers.reverse()
        sum_ok = sum(part == Part.Two, actual_sum, number, numbers, len(numbers)-2)
        if sum_ok:
            num = num + actual_sum

    # Output
    if test:
        print("Part: ", part, " Test: ", test, " correct: ", num == 3749 if part == Part.One else num == 11387)
    else:
        print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

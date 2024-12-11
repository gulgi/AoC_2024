from enum import Enum
import sys
#from tqdm import tqdm

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
    data = file.read().split(' ')

    # CODE
    num = 0
    times = 75 if part == Part.Two else 25
    for step in range(0, times):
#            print(f"{data}")
        index = 0
        while True:
            number = data[index]
            if number == '0':
                data[index] = '1'
                index = index + 1
            elif len(number) % 2 == 0:
                split = len(number) // 2
                data[index] = number[:split]
                number = str(int(number[split:]))
                data.insert(index+1, number)
                index = index + 2
            else:
                data[index] = str(int(number)*2024)
                index = index + 1
            if index >= len(data):
                break
#        print(f"{data}")
    num = len(data)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

from enum import Enum
import sys
from tqdm import tqdm
from typing import Iterable, DefaultDict

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
    """
        Brute force ....
        if part == Part.One:
            for step in tqdm(range(0, times)):
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
            num = len(data)
        else:
    """
    stones = DefaultDict(lambda: 0)
    for d in data:
        stones[int(d)] += 1

    for _ in tqdm(range(0, times)):
        new_stones = DefaultDict(lambda: 0)
        for stone_number, stone_count in stones.items():
            stone_number_str = str(stone_number)
            if stone_number == 0:
                new_stones[1] += stone_count
            elif len(stone_number_str) % 2 == 0:
                split = len(stone_number_str) // 2
                new_stones[int(stone_number_str[:split])] += stone_count
                new_stones[int(stone_number_str[split:])] += stone_count
            else:
                new_stones[stone_number*2024] += stone_count
        stones = new_stones
    num = sum(stones.values())

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()

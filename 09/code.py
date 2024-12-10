from enum import Enum
import sys
import string

class Part(Enum):
    One = 1,
    Two = 2

def print_memory(blocks):
    index = 0
    for block in blocks:
        for i in range(index, block['pos']):
            print(f".", end="")
        for i in range(0, block['blocks']):
            print(f"{block['id']}", end="")
        index = int(block['pos']) + int(block['blocks'])
    print("\n")

def calculate_checksum(blocks):
    num = 0
    for block in blocks:
        for i in range(block['pos'], block['pos']+block['blocks']):
            num = num + i * int(block['id'])
    return num

def first_free_memory(blocks, size, before):
    index = 0
    previous_block = blocks[0]
    for block in blocks:
        free_size = block['pos'] - index 
        if index < block['pos'] and free_size >= size:
            return index, previous_block
        previous_block = block
        index = block['pos'] + block['blocks']
        if before >= 0 and index >= before:
            break
    return -1, None

def defrag_one_block(blocks, free_pos, previous_block):
    last_block = blocks[-1]
    if last_block['blocks'] == 1:
        blocks.remove(last_block)
    else:
        last_block['blocks'] = last_block['blocks'] - 1

    if previous_block['id'] == last_block['id']:
        previous_block['blocks'] = previous_block['blocks'] + 1
    else:
        # create new block
        block = {}
        block['pos'] = free_pos
        block['id'] = last_block['id']
        block['blocks'] = 1
        blocks.insert(blocks.index(previous_block)+1, block)        

def defragment(blocks):
    while True:
        free_pos, previous_block = first_free_memory(blocks, 1, -1)
        if free_pos == -1:
            break
        defrag_one_block(blocks, free_pos, previous_block)

def move_blocks(blocks):
    last_id = blocks[-1]['id']
    for id in range(last_id, -1, -1):
        block = None
        for b in reversed(blocks):
            if b['id'] == id:
                block = b
                break
        if block == None:
            continue

        size = block['blocks']
        free_pos, previous_block = first_free_memory(blocks, size, block['pos'])
        if free_pos >= 0:
            blocks.remove(block)
            block['pos'] = free_pos
            blocks.insert(blocks.index(previous_block)+1, block)

def main():
    # Part 1 or 2. Test or not?
    part = Part.Two if set(["2", "two"]) & set(sys.argv) else Part.One
    test = True if "test" in sys.argv else False
    file_name = "test.txt" if test else "input.txt"

    # Read in file
    file = open(file_name)
    data = file.read()

    # massage the data
    blocks = []
    size = len(data)
    index = 0
    data_index = 0
    id = 0
    while index < size:
        block = {}
        block['pos'] = data_index
        block['id'] = id
        block['blocks'] = int(data[index])
        blocks.append(block)
        data_index = data_index + int(data[index])
        index = index + 1
        id = id + 1
        if index >= size:
            break

        free = int(data[index])
        data_index = data_index + free
        index = index + 1

    # CODE
#    print_memory(blocks)
    if part == Part.One:
        defragment(blocks)
    else:
        move_blocks(blocks)
#    print_memory(blocks)

    num = calculate_checksum(blocks)

    # Output
    print("Part: ", part, " Test: ", test)
    print("Num: ", num)

if __name__=="__main__":
    main()


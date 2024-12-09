import os
input_file = "day09/input.txt"
sample_file = "day09/sample.txt"

def defrag_and_checksum_part1(data_file) -> int:
    result = 0
    diskmap = [int(s) for s in open(data_file).read().strip()]
    disk = []

    for idx, block in enumerate(diskmap):
        if (idx % 2) == 0:
            for i in range(block):
                disk.append(str(int(idx/2)))
        else:
            for i in range(block):
                disk.append('.')
    # print(disk)
    defrag(disk)
    result = get_checksum(disk)

    return result

def defrag_and_checksum_part2(data_file) -> int:
    result = 0
    diskmap = [int(s) for s in open(data_file).read().strip()]
    disk = []

    for idx, block in enumerate(diskmap):
        if (idx % 2) == 0:
            for i in range(block):
                disk.append(str(int(idx/2)))
        else:
            for i in range(block):
                disk.append('.')
    print(disk)
    defrag2(diskmap)
    result = get_checksum(disk)

    return result

def defrag(disk: list) -> list:
    """
    Takes the list an defrags it according to the rule. Start at the end and
    fill those blocks from the front.  
    Paramters:
        disk (list): the current disk value
    Returns:
        list: defragmented list
    """
    complete = False
    spaces = []

    reversed_index = len(disk)
    print('Defragging.', end='')
    for idx, block in enumerate(reversed(disk)):
        reversed_index -= 1
        # print('.', end='')
        if block != '.' and disk.index('.') < reversed_index:
            # print('{}-{}-{}'.format(idx, block, reversed_index))
            disk[reversed_index], disk[disk.index('.')] = disk[disk.index('.')], disk[reversed_index]

    print('')
    # print(disk)
    return disk

def defrag2(diskmap: list) -> list:
    """
    Takes the list an defrags it according to the rule. Start at the end and
    fill those blocks from the front.  
    Paramters:
        disk (list): the current disk value
    Returns:
        list: defragmented list
    """

    files = []
    free = []

    for idx, value in enumerate(diskmap):
        if (idx % 2) == 0:
            files.append([int(idx/2), int(value)])
        else:
            free.append([int(idx/2), int(value)])
    print(files[0])
    print(free[0])

    return diskmap

def find_consecutive_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            duplicates.append(numbers[i])
    return duplicates

def get_checksum(disk) -> int:
    checksum = 0
    for idx, value in enumerate(disk):
        if value != '.':
            checksum += idx * int(value)

    return checksum

def cprint(text: str):
    try:
        t = os.get_terminal_size()
    except:
        t = 45
    print('─' * t.columns)
    print(text)

if __name__ == "__main__":
    # cprint('Part 1 sample: {}'.format(defrag_and_checksum_part1(sample_file)))
    # cprint('Part 1 input : {}'.format(defrag_and_checksum_part1(input_file)))
    cprint('Part 2 sample: {}'.format(defrag_and_checksum_part2(sample_file)))
    # cprint('Part 2 input : {}'.format(defrag_and_checksum_part2(input_file)))
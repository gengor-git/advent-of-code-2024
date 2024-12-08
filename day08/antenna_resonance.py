import re
input_file = "day08/input.txt"
sample_file = "day08/sample.txt"

term_size = 35
global max

def count_resonance_spots(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()
    max_x = len(data[0])
    max_y = len(data)
    global max
    max = (max_x, max_y)
    antennas = {}
    resonance = []

    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if len(re.findall(r'[\w\d]', col)) > 0:
                print(f'Antenna found: \033[33m({x}, {y})\033[0m with value {col}')
                if col in antennas:
                    antennas[col].append((x, y))
                else:
                    antennas[col] = [(x, y)]
    antinodes = []
    for freq in antennas.keys():
        print('─' * term_size)
        print(f'Frequency \033[41;33m {freq} \033[0m')
        an = get_resonance_list(antennas[freq])
        antinodes = antinodes + an

    antinodes = list(dict.fromkeys(antinodes))
    print('Antinodes found: {}'.format(len( antinodes )))

    return len(antinodes)

def get_resonance_list(coordinates: list) -> list:
    if len(coordinates) == 2:
        return get_antinodes(coordinates[0], coordinates[1])
    else:
        c1 = coordinates[0]
        my_list = []
        for c2 in coordinates[1:]:
            my_list = my_list + get_antinodes(c1, c2)
        return my_list + get_resonance_list(coordinates[1:])

def get_antinodes(loc1: tuple, loc2: tuple) -> list:
    results = []
    print('MAX       {}'.format(max))
    ax, ay = loc1[0] - loc2[0], loc1[1] - loc2[1]

    print(' Loc1     \033[32m{}\033[0m\n Loc2     \033[32m{}\033[0m'.format(loc1, loc2))
    print('Delta     \033[44;20m{}\033[0m'.format((ax, ay)))

    antinode1 = (loc1[0] + ax, loc1[1] + ay)
    antinode2 = (loc1[0] - 2*ax, loc1[1] - 2*ay)
    print('Antinode  \033[45m{}\033[0m \033[45m{}\033[0m'.format(antinode1, antinode2))

    if 0 <= antinode1[0] < max[0] and 0 <= antinode1[1] < max[1]:
        results.append(antinode1)
    if 0 <= antinode2[0] < max[0] and 0 <= antinode2[1] < max[1]:
        results.append(antinode2)

    return results

def calculate_something2(data_file) -> int:
    result = 0
    data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        pass
    return result

if __name__ == "__main__":
    print(count_resonance_spots(sample_file))
    print(count_resonance_spots(input_file))
    # print(calculate_something2(sample_file))
    # print(calculate_something2(input_file))

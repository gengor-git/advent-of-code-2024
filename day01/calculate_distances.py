input_file = "day01/input.txt"
sample_file = "day01/sample.txt"

def calculate_distances(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()
    group1 = []
    group2 = []
    for entry in data:
        line = entry.split("   ")
        group1.append(int(line[0]))
        group2.append(int(line[1]))

    group1.sort()
    group2.sort()
 
    for pos in range(len(group1)):
        if(group1[pos] < group2[pos]):
            result += group2[pos] - group1[pos]
        else:
            result += group1[pos] - group2[pos]
        
    return result


if __name__ == "__main__":
    print(calculate_distances(sample_file))
    print(calculate_distances(input_file))
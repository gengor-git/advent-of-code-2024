import re

input_file = "day03/input.txt"
sample_file = "day03/sample.txt"

reg_pattern = r"mul\(\d{1,3},\d{1,3}\)"

def mult_corrputed_memory(data_file) -> int:
    result = 0
    data = open(data_file).read().strip()
    matches = re.findall(reg_pattern, data)
    for values in matches:
        num = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", values)
        result+= int(num[0][0]) * int(num[0][1])
    return result

def calculate_something2(data_file) -> int:
    result = 0
    data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    for entry in data:
        pass
    return result

if __name__ == "__main__":
    print(mult_corrputed_memory(sample_file))
    print(mult_corrputed_memory(input_file))
    # print(calculate_something2(sample_file))
    # print(calculate_something2(input_file))

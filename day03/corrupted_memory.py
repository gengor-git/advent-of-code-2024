import re

input_file = 'day03/input.txt'
sample_file = 'day03/sample.txt'
sample_file_instr = 'day03/sample2.txt'

reg_pattern = r'mul\((\d+),(\d+)\)'
reg_remove = r'don\'t\(\)[\s\S]+?do\(\)'

def mult_corrputed_memory(data_file) -> int:
    result = 0
    data = open(data_file).read()
    print(data)
    # remove all from don't() to do()
    matches = re.findall(reg_pattern, data)
    for x, y in matches:
        result+= int(x) * int(y)
    return result

def mult_corrputed_instr_memory(data_file) -> int:
    result = 0
    data = open(data_file).read()
    # appended do is needed to as anchor for the remove regex
    data = data + 'do()'
    data = re.sub(reg_remove, '', data)
    matches = re.findall(reg_pattern, data)
    for x, y in matches:
        result+= int(x) * int(y)
    return result


if __name__ == '__main__':
    print(mult_corrputed_memory(sample_file))
    print(mult_corrputed_memory(input_file))
    print(mult_corrputed_instr_memory(sample_file_instr))
    print(mult_corrputed_instr_memory(input_file))

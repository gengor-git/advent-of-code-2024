import os

input_file = "day07/input.txt"
sample_file = "day07/sample.txt"
term_size = 15

def sum_total_calibration_results(data_file) -> int:
    print('─' * term_size)
    print('PART 1')
    result = 0
    data = [[int(line.split(':')[0]), [int(x) for x in line.split(':')[1].split()]] for line in open(data_file).read().strip().splitlines()]
    
    for idx, equation in enumerate(data):
        print('─' * term_size)
        print('EQU \033[35m{:>14}\033[0m \033[34m{}\033[0m'.format(equation[0], equation[1]))
    
    return sum(value for value, numbers in data if check_dual_equation(value, numbers))

def check_dual_equation(target: int, numbers):
    if len(numbers) == 1: # list is added/multiplied in total
        return target == numbers[0]
    a, b = numbers[:2] # first two in the array
    return (
        check_dual_equation(target, [a + b, *numbers[2:]])
        or check_dual_equation(target, [a * b, *numbers[2:]])
    )

def sum_total_calibration_results2(data_file) -> int:
    print('─' * term_size)
    print('PART 2')
    result = 0
    data = [[int(line.split(':')[0]), [int(x) for x in line.split(':')[1].split()]] for line in open(data_file).read().strip().splitlines()]
    
    for idx, equation in enumerate(data):
        print('─' * term_size)
        print('EQU \033[35m{:>14}\033[0m \033[34m{}\033[0m'.format(equation[0], equation[1]))
    
    return sum(value for value, numbers in data if check_triple_equation(value, numbers))

def check_triple_equation(target: int, numbers:list):
    if len(numbers) == 1: # list is added/multiplied in total
        return target == numbers[0]
    a, b = numbers[:2] # first two in the array
    return (
        check_triple_equation(target, [a + b, *numbers[2:]])
        or check_triple_equation(target, [a * b, *numbers[2:]])
        or check_triple_equation(target, [int(str(a) + str(b)), *numbers[2:]])
    )

if __name__ == "__main__":
    print('Part 1 sample: {:15}'.format(sum_total_calibration_results(sample_file)))
    print('Part 1 input : {:15}'.format(sum_total_calibration_results(input_file)))
    print('Part 2 sample: {:15}'.format(sum_total_calibration_results2(sample_file)))
    print('Part 2 input : {:15}'.format(sum_total_calibration_results2(input_file)))

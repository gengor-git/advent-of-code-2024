input_file = "day02/input.txt"
sample_file = "day02/sample.txt"


def count_safe_reports(data_file) -> int:
    result = 0
    reports = open(data_file).read().strip().splitlines()
    print(len(reports))
    for line in reports:
        levels = [int(level) for level in line.split()]
        # check if all are increasing
        if all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)) or all(levels[i] > levels[i + 1] for i in range(len(levels) - 1)):
            if all(abs(int(levels[i]) - int(levels[i + 1])) < 4 for i in range(len(levels) - 1)):
                result+=1
    return result


def calculate_something2(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()
    for entry in data:
        pass

    return result

if __name__ == "__main__":
    print(count_safe_reports(sample_file))
    print(count_safe_reports(input_file))
    # print(calculate_something2(sample_file))
    # print(calculate_something2(input_file))

input_file = "day02/input.txt"
sample_file = "day02/sample.txt"

def count_safe_reports(data_file) -> int:
    result = 0
    reports = open(data_file).read().strip().splitlines()
    for line in reports:
        levels = [int(level) for level in line.split()]
        if is_safe_level(levels):
            result+=1
    return result

def count_safe_reports_with_dampener(data_file) -> int:
    result = 0
    reports = open(data_file).read().strip().splitlines()
    for line in reports:
        levels = [int(level) for level in line.split()]
        if is_safe_level(levels):
            result += 1
        else:
            for i in range(len(levels)):
                copy = levels.copy()
                del copy[i]
                if is_safe_level(copy):
                   result += 1
                   break
    return result

def is_safe_level(levels) -> bool:
    results = False
    if all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)) or all(levels[i] > levels[i + 1] for i in range(len(levels) - 1)):
        if all(abs(int(levels[i]) - int(levels[i + 1])) < 4 for i in range(len(levels) - 1)):
            results = True
    return results

if __name__ == "__main__":
    print(count_safe_reports(sample_file))
    print(count_safe_reports(input_file))
    print(count_safe_reports_with_dampener(sample_file))
    print(count_safe_reports_with_dampener(input_file))

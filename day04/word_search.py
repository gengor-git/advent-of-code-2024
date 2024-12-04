import re
input_file = "day04/input.txt"
sample_file = "day04/sample.txt"


def count_xmas(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()
    # search horizontally
    for line in data:
        result += len(re.findall(r'XMAS', line))
        result += len(re.findall(r'SAMX', line))
    # search vertically
    for y in range(len(data[0])):
        line = ''.join([row[y] for row in data])
        result += len(re.findall(r'XMAS', line))
        result += len(re.findall(r'SAMX', line))

    # search diagonaly
    ''' starts with X or S
        then scan diagonnaly in all directions
        (x,y)
        x-1, y-1 TL
        x+1, y-1 TR
        x+1, y+1 BR
        x-1, y+1 BL
    '''
    max_y = len(data)-1
    max_x = len(data[0])-1
    for y in range(max_y+1):
        for x in range(max_x+1):
            t = False
            b = False
            r = False
            l = False
            if re.findall(r'X', data[y][x]):
                # print('Found X: ({}, {}) = {}'.format(x, y, re.findall(r'X|S', data[y][x])))
                if y-3>=0:
                    # we can scan above
                    t = True
                if y+3<=max_y:
                    # we can scan below
                    b = True
                if x-3>=0:
                    # we can scan left
                    l = True
                if x+3<=max_x:
                    # we can scan right
                    r = True
                if t and l:
                    # x-1, y-1 TL
                    if data[y-1][x-1] == 'M' and data[y-2][x-2] == 'A' and data[y-3][x-3] == 'S':
                        result+=1
                if t and r:
                    # x+1, y-1 TR
                    if data[y-1][x+1] == 'M' and data[y-2][x+2] == 'A' and data[y-3][x+3] == 'S':
                        result+=1
                if b and r:
                    # x+1, y-1 BR
                    if data[y+1][x+1] == 'M' and data[y+2][x+2] == 'A' and data[y+3][x+3] == 'S':
                        result+=1
                if b and l:
                    # x-1, y+1 BL
                    if data[y+1][x-1] == 'M' and data[y+2][x-2] == 'A' and data[y+3][x-3] == 'S':
                        result+=1
    return result

def count_x_mas(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()
    # search diagonaly
    ''' starts with A in the middle
        then scan diagonnaly in all directions
        (x,y)
        x-1, y-1 TL
        x+1, y-1 TR
        x+1, y+1 BR
        x-1, y+1 BL
    '''
    max_y = len(data)-1
    max_x = len(data[0])-1
    for y in range(max_y+1):
        for x in range(max_x+1):
            t = False
            b = False
            r = False
            l = False
            if re.findall(r'A', data[y][x]):
                # print('Found X: ({}, {}) = {}'.format(x, y, re.findall(r'X|S', data[y][x])))
                if y-1>=0:
                    # we can scan above
                    t = True
                if y+1<=max_y:
                    # we can scan below
                    b = True
                if x-1>=0:
                    # we can scan left
                    l = True
                if x+1<=max_x:
                    # we can scan right
                    r = True
                if t and l and b and r:
                    # x-1, y-1 TL
                    # x+1, y-1 TR
                    # x+1, y-1 BR
                    # x-1, y+1 BL
                    if (
                        (
                            data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S'
                            or data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M'
                        )
                        and
                        (
                            data[y-1][x+1] == 'M' and data[y+1][x-1] == 'S'
                            or data[y-1][x+1] == 'S' and data[y+1][x-1] == 'M'
                        )
                    ):
                        result+=1
    return result

if __name__ == "__main__":
    # print(count_xmas(sample_file))
    # print(count_xmas(input_file))
    print(count_x_mas(sample_file))
    print(count_x_mas(input_file))

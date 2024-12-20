input_file = "day06/input.txt"
sample_file = "day06/sample.txt"


def count_predicted_visits(data_file) -> int:
    room = open(data_file).read().strip().splitlines()
    
    movement = {'U': (0, -1),
            'R': (1, 0),
            'D': (0, 1),
            'L': (-1, 0)}
    next_direction = {'U': 'R',
            'R': 'D',
            'D': 'L',
            'L': 'U'}

    steps = 0
    visits = []
    current_position = (0, 0)
    next_position = (0, 0)
    current_direction = 'U'
    max_steps = 40000 # for safety
    trys = 0

    # find ^
    # start U

    for y, row in enumerate(room):
        for x, col in enumerate(row):
            # print('({}, {}): {} at ({},{{}mat(x, y, current_position, col))
            if col == '^':
                print('({}, {}): {} = START'.format(x, y, col))
                current_position = (x, y)
                next_position = (x+movement[current_direction][0], y+movement[current_direction][1])
                steps += 1

    while next_position[0] < len(room[0]) and next_position[0] >= 0 and next_position[1] < len(room) and next_position[1] >= 0 and trys < max_steps:
        trys += 1
        print('loop: \033[94m{:4}\033[0m at \033[95m{}\033[0m'.format(trys, current_position))
        look_ahead = room[next_position[1]][next_position[0]]
        if look_ahead == '#':
            print("Blocker at {}".format(next_position))
            current_direction = next_direction[current_direction]
            next_position = (current_position[0]+movement[current_direction][0], current_position[1]+movement[current_direction][1])
            print('Direction change: {}'.format(current_direction))
            print('cur: {}, next: {}'.format(current_position, next_position))
        else:
            current_position = next_position
            next_position = (current_position[0]+movement[current_direction][0], current_position[1]+movement[current_direction][1])
            print('cur: {}, next: {}'.format(current_position, next_position))
            steps += 1
            visits.append(current_position)
    return len(list(dict.fromkeys(visits)))

def count_loop_by_obstacle(data_file) -> int:
    room = open(data_file).read().strip().splitlines()
    
    movement = {'U': (0, -1),
            'R': (1, 0),
            'D': (0, 1),
            'L': (-1, 0)}
    next_direction = {'U': 'R',
            'R': 'D',
            'D': 'L',
            'L': 'U'}

    steps = 0
    current_position = (0, 0)
    next_position = (0, 0)
    starting_direction = 'U'
    current_direction = starting_direction
    max_steps = 40000 # for safety
    starting_position = (0, 0)

    for y, row in enumerate(room):
        for x, col in enumerate(row):
            if col == '^':
                print('({}, {}): {} = START'.format(x, y, col))
                current_position = starting_position = (x, y)
                next_position = (x+movement[current_direction][0], y+movement[current_direction][1])

    list_of_new_obstacles = []
    for y, row in enumerate(room):
        for x, col in enumerate(row):
            if not room[y][x] == '#':
                list_of_new_obstacles.append((x, y))

    print('Where to place obastacles: {}'.format(list_of_new_obstacles))
    loops_found = 0
    # test for each obstacle
    for obstacle in list_of_new_obstacles:
        current_position = starting_position
        current_direction = 'U'
        next_position = (starting_position[0]+movement[current_direction][0], starting_position[1]+movement[current_direction][1])
        cycle = 0
        visits = []

        print('\033[43;99mTesting manual obstacle at position \033[96m{}\033[00m'.format(obstacle))

        while next_position[0] < len(room[0]) and next_position[0] >= 0 and next_position[1] < len(room) and next_position[1] >= 0 and cycle < max_steps:
            cycle += 1
            # print('cycle: \033[94m{:4}\033[0m   at   \033[95m{}\033[0m'.format(cycle, current_position))
            look_ahead = room[next_position[1]][next_position[0]]
            if look_ahead == '#' or next_position == obstacle:
                current_direction = next_direction[current_direction]
                next_position = (current_position[0]+movement[current_direction][0], current_position[1]+movement[current_direction][1])
                # print('Direction change: {}'.format(current_direction))
                # print('cur: \033[93m{}\033[0m, next: \033[92m{}\033[0m'.format(current_position, next_position))
            elif (next_position, current_direction) in visits:
                print('\033[41;99mLoop found!\033[0m')
                loops_found+=1
                break;
            else:
                current_position = next_position
                next_position = (current_position[0]+movement[current_direction][0], current_position[1]+movement[current_direction][1])
                visits.append((current_position, current_direction))
                # print('cur: \033[93m{}\033[0m, next: \033[92m{}\033[0m'.format(current_position, next_position))

    return loops_found

if __name__ == "__main__":
    # print(count_predicted_visits(sample_file))
    # print(count_predicted_visits(input_file))
    # print(count_loop_by_obstacle(sample_file))
    print(count_loop_by_obstacle(input_file))

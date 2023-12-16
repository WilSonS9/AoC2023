import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

grid = np.array([[l[i][j] for j in range(len(l[0]))] for i in range(len(l))])

def get_directions(c, di, dj):
    if c == '.' or (c == '|' and dj == 0) or (c == '-' and di == 0):
        return [np.array([di, dj])]
    elif c == '/':
        return [np.array([-dj, -di])]
    elif c == '\\': # \ gets read as \\
        return [np.array([dj, di])]
    elif c == '|':
        dir_1 = np.array([1, 0])
        dir_2 = -dir_1
        return [dir_1, dir_2]
    elif c == '-':
        dir_1 = np.array([0, 1])
        dir_2 = -dir_1
        return [dir_1, dir_2]

def nEnergized(start_position, start_direction):
    energized  = set()
    beamStates = set()

    # pairs of form (coordinate, direction)
    # coordinate = (i, j), direction = (delta i, delta j)
    i, j   = start_position
    di, dj = start_direction

    c = grid[i, j]
    
    beams = []
    start_directions = get_directions(c, di, dj)
    for start_direction in start_directions:
        beams.append(np.array([start_position, start_direction]))

    while len(beams) > 0:
        newBeams = []
        for beam in beams:
            coordinate, direction = beam
            energized.add(tuple(coordinate))
            state = (tuple(coordinate), tuple(direction))
            if state in beamStates:
                continue

            beamStates.add(state)

            di, dj = direction

            new_i, new_j = coordinate + direction
            new_position = np.array([new_i, new_j])

            # beam is outside grid
            if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
                continue
        
            c = grid[new_i, new_j]

            new_directions = get_directions(c, di, dj)
            for new_direction in new_directions:
                newBeams.append((new_position, new_direction))
        
        beams = newBeams.copy()

    return len(energized)

start_states_top   = [(np.array([0, j]), np.array([1, 0])) for j in range(len(grid[0]))]
start_states_bot   = [(np.array([len(grid) - 1, j]), np.array([-1, 0])) for j in range(len(grid[0]))]
start_states_left  = [(np.array([i, 0]), np.array([0, 1])) for i in range(len(grid))]
start_states_right = [(np.array([i, len(grid[0]) - 1]), np.array([0, -1])) for i in range(len(grid))]

start_states = start_states_top + start_states_bot + start_states_left + start_states_right

maxEnergized = 0
for start_state in start_states:
    start_position, start_direction = start_state
    maxEnergized = max(maxEnergized, nEnergized(start_position, start_direction))

print(maxEnergized)
import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

grid        = np.array([[l[i][j] for j in range(len(l[0]))] for i in range(len(l))])
energized   = set()
beamStates  = set()

# pairs of form (coordinate, direction)
# coordinate = (i, j), direction = (delta i, delta j)
start_position  = np.array([0, 0])
if grid[0, 0] in ('.', '-'):
    start_direction = np.array([0, 1])
elif grid[0, 0] == '|':
    start_direction = np.array([1, 0])
elif grid[0, 0] == '/': # we will exit grid on next turn
    start_direction = np.array([-1, 0])
elif grid[0, 0] == '\\':
    start_direction = np.array([1, 0])
beams = [(start_position, start_direction)]

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
        
        if c == '.' or (c == '|' and dj == 0) or (c == '-' and di == 0):
            newBeams.append((new_position, direction))
        elif c == '/':
            new_direction = np.array([-dj, -di])
            newBeams.append((new_position, new_direction))
        # \ gets read as \\
        elif c == '\\':
            new_direction = np.array([dj, di])
            newBeams.append((new_position, new_direction))
        elif c == '|':
            dir_1 = np.array([1, 0])
            dir_2 = -dir_1
            newBeams.append((new_position, dir_1))
            newBeams.append((new_position, dir_2))
        elif c == '-':
            dir_1 = np.array([0, 1])
            dir_2 = -dir_1
            newBeams.append((new_position, dir_1))
            newBeams.append((new_position, dir_2))
    
    beams = newBeams.copy()

print(len(energized))
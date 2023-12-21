import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

grid = np.array([[l[i][j] for j in range(len(l[0]))] for i in range(len(l))])

start   = np.where(grid == 'S')
i_start = start[0][0]
j_start = start[1][0]

currentPositions = set()
currentPositions.add((i_start, j_start))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(64):
    newPositions = set()
    for position in currentPositions:
        i, j = position
        for d_index, d in enumerate(directions):
            i_n = i + d[0]
            j_n = j + d[1]
            if i_n < 0 or i_n >= len(grid) or j_n < 0 or j_n >= len(grid[0]) or grid[i_n, j_n] == '#':
                continue
            newPositions.add((i_n, j_n))
    currentPositions = newPositions.copy()

print(len(currentPositions))
import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

larger_inp = []

for _ in range(5):
    for line in l:
        larger_inp.append(5 * line.replace("S", "."))

grid = np.array([[larger_inp[i][j] for j in range(len(larger_inp[0]))] for i in range(len(larger_inp))])

# S is in the middle of the input
i_start = len(grid) // 2
j_start = len(grid[0]) // 2

currentPositions = set()
currentPositions.add((i_start, j_start))

directions  = [(-1, 0), (1, 0), (0, -1), (0, 1)]
grid_length = len(l) # length of one grid

# after manual inspection: grid grows in a diamond pattern from the center
# we can try using a quadratic fit
# after 65 steps, our diamond covers precisely one grid

points = []

for n in range(1, 65 + 2 * grid_length + 1):
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
    if n in (65, 65 + grid_length, 65 + 2 * grid_length):
        points.append(len(currentPositions))

# vandermonde matrix
A = np.matrix([[1, 0, 0], [1, 1, 1], [1, 2, 4]])
b = np.array(points)
x = np.linalg.solve(A, b).astype(np.int64)

# 26501365 is of the form n * grid_length + 65
# so after 26501365 steps we will be at an iteration number where we precisely cover a lot of grids with diamond shaped patterns
n = (26501365 - 65) // grid_length

print(x[0] + x[1] * n + x[2] * n**2)
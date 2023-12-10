import numpy as np
from matplotlib.path import Path

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

points = np.array([[l[i][j] for j in range(len(l[0]))] for i in range(len(l))])
# print(points)
pipes  = {'|': lambda i, j: [(i - 1, j), (i + 1, j)],
          '-': lambda i, j: [(i, j - 1), (i, j + 1)],
          'L': lambda i, j: [(i - 1, j), (i, j + 1)],
          'J': lambda i, j: [(i - 1, j), (i, j - 1)],
          '7': lambda i, j: [(i + 1, j), (i, j - 1)],
          'F': lambda i, j: [(i + 1, j), (i, j + 1)],
          '-': lambda i, j: [(i, j - 1), (i, j + 1)]}

start   = np.where(points == 'S')
i_start = start[0][0]
j_start  = start[1][0]

# manually inspect which pipe fits starting tile
points[i_start][j_start] = 'F'

adjList = {}

for i in range(len(l)):
    for j in range(len(l[0])):
        c = points[i][j]
        if not c == '.':
            neighbours = pipes[c](i, j)
            validNeighbours = []
            for neighbour in neighbours:
                i_n, j_n = neighbour
                if i_n >= 0 and i_n < len(l) and j_n >= 0 and j_n < len(l[0]):
                    validNeighbours.append((i_n, j_n))
            adjList[(i, j)] = validNeighbours

i_prev, j_prev = i_start, j_start
i, j = adjList[(i_prev, j_prev)][0]

boundary = [(i, j)]

# traverse loop
while not (i, j) == (i_start, j_start):
    neighbours = adjList[(i, j)]
    for neighbour in neighbours:
        if not neighbour == (i_prev, j_prev):
            i_prev, j_prev = i, j
            i, j = neighbour
            boundary.append((i, j))
            break

boundaryPath = Path(boundary)

n = 0

for i in range(len(l)):
    for j in range(len(l[0])):
        if boundaryPath.contains_point((i, j)) and not (i, j) in boundary:
            n += 1

print(n)
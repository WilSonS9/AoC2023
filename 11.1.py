import numpy as np
from itertools import combinations

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

points = np.array([[l[i][j] for j in range(len(l[0]))] for i in range(len(l))])

# insert extra empty rows
i = 0
while i < len(points):
    row = points[i]
    if np.all(row == '.'):
        points = np.insert(points, i, '.', axis=0)
        i += 1
    i += 1

# insert extra empty cols
i = 0
while i < len(points.T):
    col = points.T[i]
    if np.all(col == '.'):
        points = np.insert(points, i, '.', axis=1)
        i += 1
    i += 1

galaxies = []

for i in range(len(points)):
    for j in range(len(points[0])):
        c = points[i][j]
        if c == '#':
            galaxies.append((i, j))

sourceDestinationPairs = set(combinations(galaxies, r=2))

n = 0

for i, pair in enumerate(sourceDestinationPairs):
    source, dest = pair
    i_s, j_s = source
    i_d, j_d = dest

    length = abs(i_s - i_d) + abs(j_s - j_d)
    n += length

print(n)
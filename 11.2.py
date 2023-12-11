import numpy as np
from itertools import combinations

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

points = np.array([[l[i][j] for j in range(len(l[0]))] for i in range(len(l))])
empty_rows = []
empty_cols = []

i = 0
while i < len(points):
    row = points[i]
    if np.all(row == '.'):
        empty_rows.append(i)
    i += 1

i = 0
while i < len(points):
    col = points.T[i]
    if np.all(col == '.'):
        empty_cols.append(i)
    i += 1

galaxies     = []
realGalaxies = []

for i in range(len(points)):
    for j in range(len(points[0])):
        c = points[i][j]
        if c == '#':
            galaxies.append((i, j))

# calculate real coordinates after expansion
for galaxy in galaxies:
    i, j = galaxy
    i_real, j_real = i, j
    for i_er in empty_rows:
        if i > i_er:
            i_real += 1000000 - 1
    
    for j_ec in empty_cols:
        if j > j_ec:
            j_real += 1000000 - 1
    
    realGalaxies.append((i_real, j_real))

sourceDestinationPairs = set(combinations(realGalaxies, r=2))

n = 0

for i, pair in enumerate(sourceDestinationPairs):
    source, dest = pair
    i_s, j_s = source
    i_d, j_d = dest

    length = abs(i_s - i_d) + abs(j_s - j_d)
    
    n += length

print(n)
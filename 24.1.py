import numpy as np
from itertools import combinations

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

lines = []

for line in l:
    xString, vString = line.split(' @ ')
    x = tuple(map(int, xString.split(', ')[:2]))
    v = tuple(map(int, vString.split(', ')[:2]))
    lines.append((x, v))

minX = minY = 200000000000000
maxX = maxY = 400000000000000

nIntersections = 0

linePairs = set(combinations(lines, r=2))

for pair in linePairs:
    line1, line2 = pair

    x1, v1 = np.array(list(line1))
    x2, v2 = np.array(list(line2))
    
    # parallel lines never intersect (supposedly...)
    if np.linalg.det(np.matrix([v1.T, v2.T])) == 0:
        continue

    A = np.matrix([[-v2[0], v1[0]], [-v2[1], v1[1]]])
    b = np.array([x2[0] - x1[0], x2[1] - x1[1]])

    s, t = np.linalg.solve(A, b)

    # check if we crossed in the past
    if s < 0 or t < 0:
        continue
    x, y = x1 + v1 * t

    nIntersections += int(x >= minX and x <= maxX and y >= minY and y <= maxY)

print(nIntersections)
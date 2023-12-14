import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

grid = np.array([[l[i][j] for j in range(len(l[0]))] for i in range(len(l))])

def rollNorth(g):
    newGrid   = np.array([['.' for _ in range(len(l[0]))] for _ in range(len(l))])
    nRows     = len(newGrid)
    totalLoad = 0
    for j, col in enumerate(g.T):
        currentTop = 0
        for i, el in enumerate(col):
            if el == '.':
                continue
            elif el == '#':
                newGrid[i, j] = '#'
                currentTop = i + 1
            else:
                newGrid[currentTop, j] = 'O'
                totalLoad  += nRows - currentTop
                currentTop += 1
    return newGrid, totalLoad

newGrid, totalLoad = rollNorth(grid)
print(totalLoad)
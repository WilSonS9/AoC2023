import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

grid = np.array([[l[i][j] for j in range(len(l[0]))] for i in range(len(l))])

def rollNorth(g):
    newGrid   = np.array([['.' for _ in range(len(l[0]))] for _ in range(len(l))])
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
                currentTop += 1
    return newGrid

newGrid = grid.copy()

n_iterations = 1000000000

hashes = {}
hashes[hash(newGrid.data.tobytes())] = 0

jumpedAhead = False

i = 0
while i < n_iterations:
    # strategy: look for cycles and jump ahead

    # roll north
    newGrid = rollNorth(newGrid)

    # roll west
    # transpose so west is the new north
    # then roll north and transpose back
    newGrid = rollNorth(newGrid.T)
    newGrid = newGrid.T

    # roll south
    # reverse row order so south is the new north
    # then roll north and reverse row order again
    newGrid = rollNorth(np.flip(newGrid, axis=0))
    newGrid = np.flip(newGrid, axis=0)

    # roll east
    # reverse column order and transpose so east is the new north
    # then roll north, transpose back and reverse column order and we're back
    newGrid = rollNorth(np.flip(newGrid, axis=1).T)
    newGrid = np.flip(newGrid.T, axis=1)

    i += 1

    h = hash(newGrid.data.tobytes())
    if not jumpedAhead and h in hashes.keys():
        # jump ahead
        cycleLength = i - hashes[h]
        print(f'cycle found! cycle length: {cycleLength}, i = {i}')
        i += ((n_iterations - i) // cycleLength) * cycleLength
        jumpedAhead = True
    else:
        hashes[h] = i

totalLoad = 0
nRows     = len(newGrid)
for i, row in enumerate(newGrid):
    for j, el in enumerate(row):
        if el == 'O':
            totalLoad += nRows - i

print(totalLoad)
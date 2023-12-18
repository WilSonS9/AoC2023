from collections import deque 

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

boundary   = {(0, 0): True}
directions = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}

current_i, current_j = 0, 0

for line in l:
    fields    = line.split()
    direction = fields[0]
    nSteps    = int(fields[1])

    d_i, d_j = directions[direction]
    if d_j == 0:
        for d_i2 in range(1, abs(nSteps * d_i) + 1):
            boundary[(current_i + d_i * d_i2, current_j)] = True
    else:
        for d_j2 in range(1, abs(nSteps * d_j) + 1):
            boundary[(current_i, current_j + d_j * d_j2)] = True
    
    current_i += nSteps * d_i
    current_j += nSteps * d_j

# flood fill
filledCoordinates = set()
q = deque()

startNode = (-16, 9) # check manually for a node we know is inside the boundary
q.append(startNode)

while len(q) > 0:
    current_i, current_j = q.pop()
    if (current_i, current_j) in filledCoordinates:
        continue
    filledCoordinates.add((current_i, current_j))
    for direction in directions.values():
        d_i, d_j = direction
        new_i = current_i + d_i
        new_j = current_j + d_j
        if not (new_i, new_j) in boundary.keys():
            q.append((new_i, new_j))

lagoonSize = len(boundary) + len(filledCoordinates)

print(lagoonSize)
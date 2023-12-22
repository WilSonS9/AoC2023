from itertools import product
from collections import deque

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

bricks = []

for line in l:
    p1, p2 = line.split('~')

    x1, y1, z1 = map(int, p1.split(','))
    x2, y2, z2 = map(int, p2.split(','))

    coords = list(product(range(x1, x2 + 1), range(y1, y2 + 1), range(z1, z2 + 1)))

    bricks.append(coords)

bricks.sort(key=lambda el: min([x[2] for x in el]))

def dropBricks(bricks):
    newBricks = []

    coordBrickMap = {}
    supportedBy   = {i: set() for i in range(len(bricks))}
    supports      = {i: set() for i in range(len(bricks))}

    occupiedPositions = set()

    for i,brick in enumerate(bricks):
        currentCoordinates = brick.copy()

        cont = True
        while cont:

            # try to decrease all z by one
            canDecrease = True
            newCoords   = []
            for coord in currentCoordinates:
                x, y, z  = coord
                newCoord = (x, y, z - 1)

                if z - 1 < 1:
                    cont        = False
                    canDecrease = False
                    break
                elif newCoord in occupiedPositions:
                    canDecrease     = False
                    cont            = False
                    supportingBrick = coordBrickMap[newCoord]
                    supportedBy[i].add(supportingBrick)
                    supports[supportingBrick].add(i)
                
                newCoords.append(newCoord)
            
            if canDecrease:
                currentCoordinates = newCoords.copy()
        
        for coord in currentCoordinates:
            occupiedPositions.add(coord)
            coordBrickMap[coord] = i

        newBricks.append(currentCoordinates)

    return newBricks, supportedBy, supports

newBricks, supportedBy, supports = dropBricks(bricks)

def nFalls(i):
    q = deque()
    removedBricks = set()
    removedBricks.add(i)
    
    for neighbour in supports[i]:
        q.append(neighbour)

    while len(q) > 0:
        currentBrick = q.popleft()
        neighbours   = supportedBy[currentBrick]
        supported    = supports[currentBrick]

        if all(neighbour in removedBricks for neighbour in neighbours):
            removedBricks.add(currentBrick)
            for support in supported:
                q.append(support)

    # - 1 since we don't count the brick itself
    return len(removedBricks) - 1

s = sum(map(nFalls, range(len(newBricks))))
print(s)
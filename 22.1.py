from itertools import product

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

s = 0

for supportedByBrick in supports.values():
    canBeRemoved = True

    # can be removed iff all bricks supported by this brick are supported by some other brick
    for supportedBrickIndex in supportedByBrick:
        if len(supportedBy[supportedBrickIndex]) == 1:
            canBeRemoved = False
            break
    
    s += int(canBeRemoved)

print(s)
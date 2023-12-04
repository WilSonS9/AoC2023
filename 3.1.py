with open('inp.txt', 'r') as f:
    l = list(map(lambda s: list(s), f.read().split('\n')))

nRows = len(l)
nCols = len(l[0])

notSymbols = '1234567890.'

def readNum(i, j):
    currentNum = l[i][j]
    
    jRight = j + 1
    jLeft  = j - 1

    # read all chars to the right
    while jRight < nCols:
        c = l[i][jRight]
        if c.isdigit():
            currentNum += c
            jRight     += 1
        else:
            break
    
    # and all chars to the left
    while jLeft >= 0:
        c = l[i][jLeft]
        if c.isdigit():
            currentNum = c + currentNum
            jLeft      -= 1
        else:
            break
    
    # return the number as well as start and end indices
    return int(currentNum), jLeft + 1, jRight - 1

def isAdjacent(i, j):
    coords = [(i + di, j + dj) for dj in range(-1, 2) for di in range(-1, 2)]
    for coord in coords:
        ci, cj = coord
        if ci < nRows and ci >= 0 and cj < nCols and cj >= 0:
            c = l[ci][cj]
            if c not in notSymbols:
                return True
    return False

nums = []
validNums = []

for i in range(nRows):
    j = 0
    while j < nCols:
        c = l[i][j]
        if c.isdigit():
            currentNum, jLeft, jRight = readNum(i, j)
            adjacent = isAdjacent(i, j)
            if adjacent:
                currentNum, jLeft, jRight = readNum(i, j)
                validNums.append(currentNum)
                j = jRight + 1
            else:
                currentNum, jLeft, jRight = readNum(i, j)
                j += 1
        else:
           j += 1

print(sum(validNums))
with open('inp.txt', 'r') as f:
    l = list(map(lambda s: list(s), f.read().split('\n')))

nRows = len(l)
nCols = len(l[0])

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


def gearProduct(i, j):
    coords = [(i + di, j + dj) for dj in range(-1, 2) for di in range(-1, 2)]

    nums = {}
    for coord in coords:
        ci, cj = coord
        if ci < nRows and ci >= 0 and cj < nCols and cj >= 0:
            c = l[ci][cj]
            if c.isdigit():
                currentNum, jLeft, _ = readNum(ci, cj)
                nums[(ci, jLeft)] = currentNum
    if len(nums.keys()) == 2:
        p = 1
        for _,val in nums.items():
            p *= val
        return p
    else:
        return 0

nums = []
validNums = []
s = 0
for i in range(nRows):
    j = 0
    while j < nCols:
        c = l[i][j]
        if c == '*':
            p = gearProduct(i, j)
            s += p
        j += 1

print(s)
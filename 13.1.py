import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n\n')

patterns = []

for pattern in l:
    patternLines = pattern.split('\n')
    points = np.array([[patternLines[i][j] for j in range(len(patternLines[0]))] for i in range(len(patternLines))])
    patterns.append(points)

def checkReflection(pattern):
    #check row reflection
    for i in range(1, len(pattern)):
        lower, upper = pattern[:i], pattern[i:]
        if i < len(pattern) - i:
            upper = upper[:i]
        else:
            lower = lower[i - len(pattern):]
        
        if (lower == upper[::-1]).all():
            return i

    # if no reflection found
    return 0

s = 0

for pattern in patterns:
    rowReflectionIndex = checkReflection(pattern)
    s += 100 * rowReflectionIndex
    if rowReflectionIndex == 0:
        colReflectionIndex = checkReflection(pattern.T)
        s += colReflectionIndex

print(s)
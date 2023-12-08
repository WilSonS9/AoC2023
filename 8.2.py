from math import lcm

with open('inp.txt', 'r') as f:
    l = f.read().split('\n\n')

pattern = l[0]
adjList = {}

sources = []

for line in l[1].split('\n'):
    lineFiltered       = line.replace('(', '').replace(')', '')
    source, destString = lineFiltered.split(' = ')
    lDest, rDest       = destString.split(', ')

    if source[-1] == 'A':
        sources.append(source)

    adjList[source] = (lDest, rDest)

currentState = sources

nSteps = []

for source in sources:
    i           = 0
    currentNode = source
    while True:

        oldNode = currentNode
        if pattern[i % len(pattern)] == 'L':
            currentNode = adjList[currentNode][0]
        else:
            currentNode = adjList[currentNode][1]
        
        i += 1

        if currentNode[-1] == 'Z':
            nSteps.append(i)
            break

# assume input is cyclic
print(lcm(*nSteps))
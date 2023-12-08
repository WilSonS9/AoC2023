with open('inp.txt', 'r') as f:
    l = f.read().split('\n\n')

pattern = l[0]
adjList = {}

for line in l[1].split('\n'):
    lineFiltered       = line.replace('(', '').replace(')', '')
    source, destString = lineFiltered.split(' = ')
    lDest, rDest       = destString.split(', ')

    adjList[source] = (lDest, rDest)

currentNode = 'AAA'
destination = 'ZZZ'

i = 0

while True:
    oldNode = currentNode
    if pattern[i % len(pattern)] == 'L':
        currentNode = adjList[currentNode][0]
    else:
        currentNode = adjList[currentNode][1]
    
    i += 1

    if currentNode == destination:
        break

print(i)
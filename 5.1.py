with open('inp.txt', 'r') as f:
    l = f.read().split('\n\n')

seeds = list(map(int, l[0].split(': ')[1].split(' ')))

maps = [[] for _ in range(7)]

for i, line in enumerate(l[1:]):
    rows = line.split('\n')
    for row in rows[1:]:
        destination, source, length = list(map(int, row.split(' ')))
        maps[i].append((source, destination, length))

locations = []

for seed in seeds:
    currentNode = seed
    for i in range(len(maps)):
        oldNode = currentNode
        for mapRange in maps[i]:
            source, destination, length = mapRange
            if currentNode >= source and currentNode < (source + length):
                currentNode = destination + currentNode - source
                break
        print(f'    {oldNode} ---> {currentNode}')
    print(f'Start: {seed}, End: {currentNode}')
    locations.append(currentNode)

print(min(locations))
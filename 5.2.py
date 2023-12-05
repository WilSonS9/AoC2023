with open('inp.txt', 'r') as f:
    l = f.read().split('\n\n')

seeds = list(map(int, l[0].split(': ')[1].split(' ')))

seedPairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

maps = [[] for _ in range(7)]

for i, line in enumerate(l[1:]):
    rows = line.split('\n')
    for row in rows[1:]:
        destination, source, length = list(map(int, row.split(' ')))
        maps[i].append((source, destination, length))
    print(rows[1:])

# now we go in reverse, find the lowest output that matches to an input
maps = maps[::-1]

# answer will be the lowest s-value that matches to an input
# takes around 10-15 minutes on my machine
s = 0
cont = True
while cont:
    if s % 100_000 == 0:
        print(f's={s}')
    currentNode = s
    for i in range(len(maps)):
        oldNode = currentNode
        for mapRange in maps[i]:
            source, destination, length = mapRange
            if currentNode >= destination and currentNode < (destination + length):
                currentNode = source + currentNode - destination
                break
        # print(f'    {oldNode} ---> {currentNode}')
    # print(f'Start: {s}, End: {currentNode}')
    for pair in seedPairs:
        start, length = pair
        if currentNode >= start and currentNode < start + length:
            print(f'finished in range {pair} with s={s}')
            print(f'end at seed={currentNode}')
            cont = False
            break
    s += 1
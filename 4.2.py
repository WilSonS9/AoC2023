with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

def matching(ticket, winningNums):
    matching = 0
    for n in ticket:
        if n in winningNums:
            matching += 1
    return matching

s = 0

ticketMap = {num: 1 for num in range(1, len(l) + 1)}

for i, line in enumerate(l):
    gameNum = i + 1

    mul = ticketMap[gameNum]

    vals = line.replace('  ', ' ').split(': ')[1]
    fields = vals.split(' | ')
    scratchNums = list(map(int, fields[0].split(' ')))
    winningNums = list(map(int, fields[1].split(' ')))

    matches = matching(scratchNums, winningNums)

    for num in range(gameNum + 1, gameNum + matches + 1):
        if num in ticketMap:
            ticketMap[num] += mul
        else:
            ticketMap[num] = mul

print(sum(ticketMap.values()))
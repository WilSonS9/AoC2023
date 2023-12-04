with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

def points(ticket, winningNums):
    matching = 0
    for n in ticket:
        if n in winningNums:
            matching += 1
    if matching == 0:
        return 0
    else:
        return 2**(matching - 1)

s = 0

for line in l:
    vals = line.replace('  ', ' ').split(': ')[1]
    fields = vals.split(' | ')
    scratchNums = list(map(int, fields[0].split(' ')))
    winningNums = list(map(int, fields[1].split(' ')))

    s += points(scratchNums, winningNums)

print(s)
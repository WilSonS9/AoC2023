with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

s = 0

for line in l:
    sequence = list(map(int, line.split(' ')))

    sequences = [sequence]
    while True:
        diffs           = []
        currentSequence = sequences[-1]
        for i in range(len(currentSequence) - 1):
            diffs.append(currentSequence[i + 1] - currentSequence[i])
        if not any(currentSequence):
            break
        sequences.append(diffs)

    sequences[-1].append(0)

    i = len(sequences) - 2
    for _ in range(len(sequences) - 1):
        currentSequence  = sequences[i]
        previousSequence = sequences[i + 1]

        extrapolatedValue = currentSequence[0] - previousSequence[0]

        sequences[i] = [extrapolatedValue] + currentSequence
        i -= 1

    s += sequences[0][0]

print(s)
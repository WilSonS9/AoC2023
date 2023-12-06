# I just manually changed the input and used the same code as part 1

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

times = list(map(int, l[0].split()[1:]))
dists = list(map(int, l[1].split()[1:]))

p = 1

for i in range(len(times)):
    time = times[i]
    dist = dists[i]

    nWays = 0

    for t in range(time):
        d = t * (time - t)
        if d > dist:
            nWays += 1

        # concave function (if t was continous), decreasing after we reach our maximum
        # so we don't need to check the final values
        elif d < dist and nWays > 0:
            break
    p *= nWays

print(p)
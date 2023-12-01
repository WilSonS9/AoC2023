with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

d = map(lambda line: list(filter(lambda c: c.isdigit(), line)), l)

nums = map(lambda ds: int(ds[0] + ds[-1]), d)

print(sum(nums))
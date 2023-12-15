from functools import reduce

with open('inp.txt', 'r') as f:
    l = f.read().split(',')

def h(s):
    return reduce(lambda a, b: 17 * (a + ord(b)) % 256, s, 0)

s = sum(map(h, l))
print(s)
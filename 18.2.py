with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

vertices     = [(0, 0)]
directions   = {'0': (0, 1), '1': (-1, 0), '2': (0, -1), '3': (1, 0)}
len_boundary = 1

current_i, current_j = 0, 0

for line in l:
    fields    = line.split()
    hexString = fields[2]
    direction = hexString[-2]
    nSteps    = int(hexString[2:-2], 16)

    d_i, d_j = directions[direction]
    
    current_i += nSteps * d_i
    current_j += nSteps * d_j

    vertices.append((current_i, current_j))
    len_boundary += nSteps

A = 0

# shoelace formula
for i in range(len(vertices)):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % len(vertices)] # to include the last case
    A += x1 * y2 - y1 * x2

print(int(abs(A) / 2 + len_boundary // 2 + 1))
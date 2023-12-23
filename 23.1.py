import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

adjList = {}

G = nx.DiGraph()

for i,row in enumerate(l):
    for j,c in enumerate(row):
        if c == '#':
            continue

        neighbours = []

        if c in directions.keys():
            direction = directions[c]
            i_n       = i + direction[0]
            j_n       = j + direction[1]
            neighbours.append((i_n, j_n))
            G.add_edge((i, j), (i_n, j_n))
        else:
            for d in directions.values():
                i_n = i + d[0]
                j_n = j + d[1]

                if i_n < 0 or i_n >= len(l) or j_n < 0 or j_n >= len(l[0]) or l[i_n][j_n] == '#':
                    continue
                neighbours.append((i_n, j_n))
                G.add_edge((i, j), (i_n, j_n))

        adjList[(i, j)] = neighbours

start = (0, l[0].index('.'))
end   = (len(l) - 1, l[-1].index('.'))

paths         = nx.all_simple_paths(G, start, end)
maxPathLength = 0
for path in paths:
    maxPathLength = max(maxPathLength, len(path) - 1)

print(maxPathLength)
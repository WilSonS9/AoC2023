import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

adjList = {}
weights = {}

for i,row in enumerate(l):
    for j,c in enumerate(row):
        if c == '#':
            continue

        neighbours = []

        for d in directions.values():
            i_n = i + d[0]
            j_n = j + d[1]

            if i_n < 0 or i_n >= len(l) or j_n < 0 or j_n >= len(l[0]) or l[i_n][j_n] == '#':
                continue
            neighbours.append((i_n, j_n))
            weights[((i, j), (i_n, j_n))] = weights[((i_n, j_n), (i, j))] = 1

        adjList[(i, j)] = neighbours

# replace all nodes of the form u -> v -> w with u -> w since v doesn't contribute anything meaningful
# also update weights so weight(u, w) = weight(u, v) + weight(v, w)
cont = True
while cont:
    cont = False
    for node, neighbours in adjList.items():
        if len(neighbours) == 2:
            del adjList[node]
            adjList[neighbours[0]].append(neighbours[1])
            adjList[neighbours[0]].remove(node)
            adjList[neighbours[1]].append(neighbours[0])
            adjList[neighbours[1]].remove(node)

            weights[(neighbours[0], neighbours[1])] = weights[(neighbours[1], neighbours[0])] = weights[(node, neighbours[0])] + weights[(node, neighbours[1])]
            del weights[(neighbours[0], node)]
            del weights[(node, neighbours[0])]
            del weights[(neighbours[1], node)]
            del weights[(node, neighbours[1])]
            cont = True
            break

G = nx.Graph()

for node, neighbours in adjList.items():
    for neighbour in neighbours:
        G.add_edge(node, neighbour, weight=weights[(node, neighbour)])

start = (0, l[0].index('.'))
end   = (len(l) - 1, l[-1].index('.'))

paths         = nx.all_simple_paths(G, start, end)
maxPathLength = 0
for path in paths:
    weight        = nx.path_weight(G, path, weight='weight')
    maxPathLength = max(maxPathLength, weight)

print(maxPathLength)
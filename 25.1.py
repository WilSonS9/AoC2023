import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

G = nx.Graph()
for line in l:
    source, destinationsString = line.split(': ')
    destinations = destinationsString.split(' ')
    for destination in destinations:
        G.add_edge(source, destination)

disconnect = nx.minimum_edge_cut(G)

for u,v in disconnect:
    G.remove_edge(u, v)

p = 1
for island in nx.connected_components(G):
    p *= len(island)

print(p)
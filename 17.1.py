from queue import PriorityQueue
import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

grid = np.array([[int(l[i][j]) for j in range(len(l[0]))] for i in range(len(l))])

start   = (0, 0)
end     = (len(grid) - 1, len(grid[0]) - 1)
visited = set()

# directions
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pq = PriorityQueue()
pq.put((0, start, None, 0))  # (distance, node, direction, steps_in_direction)
    
while not pq.empty():
    dist, node, prev_direction, steps = pq.get()
    if node == end:
        print(dist)
        break

    for d_index, d in enumerate(directions):
        i_n = node[0] + d[0]
        j_n = node[1] + d[1]
        if i_n < 0 or i_n >= len(grid) or j_n < 0 or j_n >= len(grid[0]):
            continue
        elif prev_direction != None and d[0] == -directions[prev_direction][0] and d[1] == -directions[prev_direction][1]:
            continue
        elif d_index == prev_direction and steps == 3:
            continue
        
        weight    = grid[i_n, j_n]
        neighbour = (i_n, j_n)

        new_dist = dist + weight

        if d_index != prev_direction:
            new_steps = 1
        else:
            new_steps = steps + 1

        if (neighbour, d_index, new_steps) in visited:
            continue
        
        visited.add((neighbour, d_index, new_steps))
        
        pq.put((new_dist, neighbour, d_index, new_steps))
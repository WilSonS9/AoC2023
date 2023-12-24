import numpy as np
from sympy import Symbol
from sympy import solve_poly_system

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

lines = []

for line in l:
    xString, vString = line.split(' @ ')
    x = tuple(map(int, xString.split(', ')))
    v = tuple(map(int, vString.split(', ')))
    lines.append((x, v))

x  = Symbol('x')
y  = Symbol('y')
z  = Symbol('z')
vx = Symbol('vx')
vy = Symbol('vy')
vz = Symbol('vz')

eqs    = []
t_syms = []

# there is only one line that intersects three other lines at any points
# since we know there is a solution, we just need to guarantee intersection with the first three lines
# and it will automatically be our solution
for i,line in enumerate(lines[:3]):
    t_sym = Symbol(f't{i}')

    xs,  vs       = line
    x1,  y1,  z1  = xs
    vx1, vy1, vz1 = vs

    eqs.append(x1 + vx1 * t_sym - x - vx * t_sym)
    eqs.append(y1 + vy1 * t_sym - y - vy * t_sym)
    eqs.append(z1 + vz1 * t_sym - z - vz * t_sym)

    t_syms.append(t_sym)

solution = solve_poly_system(eqs, *([x,y,z,vx,vy,vz] + t_syms))
x_sol    = [solution[0][i] for i in range(3)]
print(sum(x_sol))
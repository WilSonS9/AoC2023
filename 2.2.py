with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

# return power of minimum set of cubes
def gamePossible(gameString):
    draws  = gameString.split(':')[1].split(';')

    minCubes = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            a = cube.lstrip().split(' ')
            nCubes = int(a[0])
            color  = a[1]
            minCubes[color] = max(minCubes[color], nCubes)
    return minCubes['red'] * minCubes['green'] * minCubes['blue']

possibleGames = map(lambda g: gamePossible(g), l)
print(sum(possibleGames))
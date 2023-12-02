with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

maxCubes = {'red': 12, 'green': 13, 'blue': 14}

# return 0 if game not possible, else return game id
def gamePossible(gameString):
    fields = gameString.split(':')
    draws  = fields[1].split(';')
    gameId = int(fields[0].split(' ')[-1])
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            a = cube.lstrip().split(' ')
            nCubes = int(a[0])
            color  = a[1]
            if nCubes > maxCubes[color]:
                return 0
    return gameId

possibleGames = map(lambda g: gamePossible(g), l)
print(sum(possibleGames))
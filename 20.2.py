from collections import deque
from math import lcm

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

modules = {}

for line in l:
    source, destinationsStr = line.split(' -> ')
    destinations            = destinationsStr.split(', ')

    moduleType = source[0]
    if moduleType == '%':
        name          = source[1:]
        modules[name] = {'type': 'flip-flop', 'state': False, 'destinations': destinations}
    elif moduleType == '&':
        name          = source[1:]
        modules[name] = {'type': 'conjunction', 'memory': {}, 'destinations': destinations}
    else:
        modules[source] = {'type': 'broadcast', 'destinations': destinations}

output = 'rx'

# add conjunction connections
for key, module in modules.items():
    for destination in module['destinations']:
        if destination == output:
            continue
        destinationModule = modules[destination]
        if destinationModule['type'] == 'conjunction':
            destinationModule['memory'][key] = False

modules[output] = {'type': 'output'}

signalStrings = {False: '-low', True: '-high'}

outputParent = 'bq'

# only parent of output is a conjunction module
# it will send a low signal iff all its connections are sending high signals
# idea: count how many presses it takes for each of the connections to send high signals to this conjunction module
# and take lcm of these

nButtonPresses = {destination: 0 for destination in modules[outputParent]['memory'].keys()}

def pressButton(i):
    q = deque()

    for destination in modules['broadcaster']['destinations']:
        q.append(('broadcaster', False, destination))

    while len(q) > 0:
        source, signalType, destination = q.popleft()

        destinationModule = modules[destination]

        if destinationModule['type'] == 'output':
            continue

        if destinationModule['type'] == 'flip-flop':
            if not signalType:
                destinationModule['state'] = not destinationModule['state']
                for neighbour in destinationModule['destinations']:
                    q.append((destination, destinationModule['state'], neighbour))
        elif destinationModule['type'] == 'conjunction':
            memory         = destinationModule['memory']
            memory[source] = signalType
            if all(memory.values()):
                newSignalType = False
            else:
                newSignalType = True

                if destination in nButtonPresses.keys():
                    if nButtonPresses[destination] == 0:
                        nButtonPresses[destination] = i
            
            for neighbour in destinationModule['destinations']:
                q.append((destination, newSignalType, neighbour))

i = 1
while True:
    pressButton(i)
    
    # if we have gotten the cycle length for all conjunctions to parent of output
    if all(map(lambda nPresses: nPresses > 0, nButtonPresses.values())):
        print(lcm(*nButtonPresses.values()))
        break

    i += 1
from collections import deque

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

def pressButton():
    nLowPulses  = 1 # from pressing the button, sending -low to broadcaster
    nHighPulses = 0

    q = deque()

    for destination in modules['broadcaster']['destinations']:
        q.append(('broadcaster', False, destination))

    while len(q) > 0:
        source, signalType, destination = q.popleft()

        destinationModule = modules[destination]

        nHighPulses += int(signalType)
        nLowPulses  += int(not signalType)

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
            
            for neighbour in destinationModule['destinations']:
                q.append((destination, newSignalType, neighbour))
    
    return (nLowPulses, nHighPulses)

nLowPulses = nHighPulses = 0

for _ in range(1000):
    newLowPulses, newHighPulses = pressButton()
    
    nLowPulses  += newLowPulses
    nHighPulses += newHighPulses

print(nLowPulses * nHighPulses)
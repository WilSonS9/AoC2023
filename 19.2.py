from copy import deepcopy

with open('inp.txt', 'r') as f:
    workflowsStr, partsStr = f.read().split('\n\n')

workflows = {}

for workflowStr in workflowsStr.split('\n'):
    fields  = workflowStr[:-1].split('{')
    name    = fields[0]
    filters = fields[1].split(',')

    filterList = []
    for filter in filters[:-1]:
        filterOperation, destination = filter.split(':')
        if '>' in filter:
            operand = '>'
        else:
            operand = '<'
        
        category, value = filterOperation.split(operand)
        filterList.append((category, int(value), operand, destination))
    
    otherwise = filters[-1]

    workflows[name] = {'filters': filterList, 'otherwise': otherwise}

ranges = {}
for category in ['x', 'm', 'a', 's']:
    ranges[category] = (1, 4000)

def rangeSize(ranges):
    size = 1
    for rangeMin, rangeMax in ranges.values():
        size *= rangeMax - rangeMin + 1
    return size

def nWays(ranges, currentWorkflow):
    filters = currentWorkflow['filters']

    n = 0

    currentRange = deepcopy(ranges)

    # number of ways to get accepted = number of ways if we pass the filter + number of ways if we don't pass the filter
    for filter in filters:
        category, value, operand, destination = filter

        passRange = deepcopy(currentRange)
        oldMin, oldMax = passRange[category]

        if operand == '>':
            newMin = value + 1
            newMax = oldMax

            failMax = value
            failMin = oldMin
        else:
            newMax = value - 1
            newMin = oldMin

            failMax = oldMax
            failMin = value
        
        passRange[category] = (newMin, newMax)

        # number of ways if we pass the filter
        if newMin <= oldMax:
            if destination == 'A':
                n += rangeSize(passRange)
            elif destination != 'R':
                n += nWays(passRange, workflows[destination])
        
        # the ranges if we fail the filter
        currentRange[category] = (failMin, failMax)
    
    # number of ways if we fail all filters
    destination = currentWorkflow['otherwise']
    if destination == 'A':
        n += rangeSize(currentRange)
    elif destination != 'R':
        n += nWays(currentRange, workflows[destination])
    
    return n
        
print(nWays(ranges, workflows['in']))
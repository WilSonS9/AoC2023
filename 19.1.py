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
    
s = 0

for partStr in partsStr.split('\n')[:]:
    categoryValues = {}

    fields = partStr[1:-1].split(',')
    for field in fields:
        category, value = field.split('=')
        categoryValues[category] = int(value)

    currentWorkflow = workflows['in']

    cont = True
    while cont:
        filters    = currentWorkflow['filters']
        hasMatched = False
        for filter in filters:
            category, value, operand, destination = filter

            if operand == '>':
                if categoryValues[category] > value:
                    nextWorklowName = destination
                    hasMatched      = True
            else:
                if categoryValues[category] < value:
                    nextWorklowName = destination
                    hasMatched      = True
            
            if hasMatched and nextWorklowName == 'R':
                cont = False
                break
            elif hasMatched and nextWorklowName == 'A':
                cont = False
                s += sum(categoryValues.values())
                break
            elif hasMatched:
                currentWorkflow = workflows[nextWorklowName]
                break
        
        if not hasMatched:
            nextWorklowName = currentWorkflow['otherwise']
            if nextWorklowName == 'R':
                cont = False
            elif nextWorklowName == 'A':
                cont = False
                s += sum(categoryValues.values())
            else:
                currentWorkflow = workflows[nextWorklowName]
        
print(s)
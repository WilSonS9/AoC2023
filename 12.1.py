from functools import cache

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

rowGroupPairs = []

for line in l:
    row, nums = line.split(' ')
    groups = tuple(map(int, nums.split(','))) # use tuple as it is a hashable type for cache
    rowGroupPairs.append((row, groups))

@cache
def nWays(row, groupsLeft, currentGroupSize):
    # base case for our recursion
    # if we should have no more groups and we are not currently in a group, this combination is valid
    # if we should have one more group and it is the same size as the one we are currently in, this is also valid
    # else, this combination is invalid
    if len(row) == 0:
        if (len(groupsLeft) == 0 and currentGroupSize == 0) or (len(groupsLeft) == 1 and currentGroupSize == groupsLeft[0]):
            return 1
        else:
            return 0
    
    # if our current group is larger than it should or if we are in a group even though we shouldn't have any more groups
    # then the combination is invalid and we don't need to calculate further
    if (len(groupsLeft) > 0 and currentGroupSize > groupsLeft[0]) or (len(groupsLeft) == 0 and currentGroupSize > 0):
        return 0

    n = 0

    currentSpring = row[0]

    # number of valid ways if current spring were to be damaged
    if currentSpring == '#' or currentSpring == '?':
        n += nWays(row[1:], groupsLeft, currentGroupSize + 1)

    # number of valid ways if current spring were to be operational
    if currentSpring == '.' or currentSpring == '?':
        if len(groupsLeft) > 0 and currentGroupSize == groupsLeft[0]:
            n += nWays(row[1:], groupsLeft[1:], 0)
        elif currentGroupSize == 0:
            n += nWays(row[1:], groupsLeft, 0)
    
    return n

n = 0
for pair in rowGroupPairs:
    row, group = pair
    n += nWays(row, group, 0)

print(n)
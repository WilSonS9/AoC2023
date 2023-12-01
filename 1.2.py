with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

m = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def min_max_digits(line):
    reversed = line[::-1]

    min_i          = 100000000
    min_reversed_i = 100000000

    min_dig = ''
    max_dig = ''

    for key,value in m.items():
        i          = line.find(key)
        i_reversed = reversed.find(key[::-1])

        if i < min_i and i >= 0:
            min_dig = str(value)
            min_i   = i

        if i_reversed < min_reversed_i and i_reversed >= 0:
            max_dig        = str(value)
            min_reversed_i = i_reversed

    return [min_dig, max_dig]

d = map(lambda line: min_max_digits(line), l)

nums = map(lambda ds: int(ds[0] + ds[-1]), d)

print(sum(nums))
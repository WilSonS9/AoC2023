from functools import reduce

with open('inp.txt', 'r') as f:
    l = f.read().split(',')

def h(s):
    return reduce(lambda a, b: 17 * (a + ord(b)) % 256, s, 0)

# key: label, value: (boxN, focalLength)
labels = {}

# boxes[i] contains the labels of the lenses in box i
boxes  = [[] for _ in range(256)]

for st in l:
    if '=' in st:
        label, focalLength = st.split('=')
        boxN               = h(label)

        # if no lens with this label is in a box
        if not label in labels.keys() or labels[label] == None:
            boxes[boxN].append(label)

        labels[label] = (boxN, int(focalLength))
    else:
        label = st[:-1]

        # if label is in a box
        if label in labels.keys() and not labels[label] is None:
            currentBox, _ = labels[label]
            boxes[currentBox].remove(label)
            labels[label] = None

s = 0

for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        focalLength = labels[lens][1]
        s += (i + 1) * (j + 1) * focalLength

print(s)
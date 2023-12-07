with open('inp.txt', 'r') as f:
    l = f.read().split()

class hand:
    def __init__(self, cards):
        self.cards = cards

    def __lt__(self, other):
        hand1 = self.cards
        hand2 = other.cards

        types = {hand1: 0, hand2: 0}
        for hand in [hand1, hand2]:
            handSymbols = list(set(hand))
            if len(handSymbols) == 1:
                types[hand] = 0
            elif len(handSymbols) == 2:
                if hand.count(handSymbols[0]) == 4 or hand.count(handSymbols[1]) == 4:
                    types[hand] = 1
                else:
                    types[hand] = 2
            elif len(handSymbols) == 3:
                if hand.count(handSymbols[0]) == 3 or hand.count(handSymbols[1]) == 3 or hand.count(handSymbols[2]) == 3:
                    types[hand] = 3
                else:
                    types[hand] = 4
            elif len(handSymbols) == 4:
                types[hand] = 5
            else:
                types[hand] = 6

        if types[hand1] < types[hand2]:
            return True
        elif types[hand1] > types[hand2]:
            return False
        else:
            for i in range(5):
                i1 = symbols.index(hand1[i])
                i2 = symbols.index(hand2[i])
                if i1 < i2:
                    return True
                elif i1 > i2:
                    return False
            return False
    
    def __repr__(self):
        return self.cards

cards = [(hand(l[i]), int(l[i + 1])) for i in range(0, len(l), 2)]

symbols = 'AKQJT98765432'

cards = sorted(cards, key=lambda pair: pair[0], reverse=True)

s = 0

for i,pair in enumerate(cards):
    s += (i + 1) * pair[1]

print(s)
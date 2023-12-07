with open('inp.txt', 'r') as f:
    l = f.read().split()

def bestHand(hand):
    # (very) ugly way to do this but whatever
    # atleast it's fast :-)
    handSymbols = set(hand)
    if hand.count('J') == 0:
        # no choice available
        return hand

    elif hand.count('J') == 5:
        # go for 5 of a kind
        return 'AAAAA'

    elif hand.count('J') == 4:
        # go for 5 of a kind
        otherSymbs = list(handSymbols.difference(set('J')))
        newHand = hand.replace('J', otherSymbs[0])
        return newHand

    elif hand.count('J') == 3:
        # go for 4 or 5 of a kind
        otherSymbs = list(handSymbols.difference(set('J')))
        newHand = hand.replace('J', otherSymbs[0])
        return newHand

    elif hand.count('J') == 2:
        otherSymbs = list(handSymbols.difference(set('J')))
        if len(otherSymbs) == 1:
            # go for 5 of a kind
            newHand = hand.replace('J', otherSymbs[0])
            return newHand
        elif len(otherSymbs) == 2:
            # go for 4 of a kind
            if hand.count(otherSymbs[0]) == 2:
                newHand = hand.replace('J', otherSymbs[0])
                return newHand
            else:
                newHand = hand.replace('J', otherSymbs[1])
                return newHand
        else:
            # go for 3 of a kind since no better option is available
            newHand = hand.replace('J', otherSymbs[0])
            return newHand

    else:
        otherSymbs = list(handSymbols.difference(set('J')))
        if len(otherSymbs) == 1:
            # go for 5 of a kind
            newHand = hand.replace('J', otherSymbs[0])
            return newHand
        elif len(otherSymbs) == 2:
            # go for 4 of a kind
            if hand.count(otherSymbs[0]) == 3:
                newHand = hand.replace('J', otherSymbs[0])
                return newHand
            elif hand.count(otherSymbs[1]) == 3:
                newHand = hand.replace('J', otherSymbs[1])
                return newHand
            # or full house if 4 of a kind not available
            else:
                newHand = hand.replace('J', otherSymbs[0])
                return newHand
        elif len(otherSymbs) == 3:
            # go for 3 of a kind
            if hand.count(otherSymbs[0]) == 2:
                newHand = hand.replace('J', otherSymbs[0])
                return newHand
            elif hand.count(otherSymbs[1]) == 2:
                newHand = hand.replace('J', otherSymbs[1])
                return newHand
            else:
                newHand = hand.replace('J', otherSymbs[2])
                return newHand
        elif len(otherSymbs) == 4:
            # go for one pair
            newHand = hand.replace('J', otherSymbs[0])
            return newHand

def handType(hand):
    type = 0
    handSymbols = list(set(hand))

    if len(handSymbols) == 1:
        type = 0
    elif len(handSymbols) == 2:
        if hand.count(handSymbols[0]) == 4 or hand.count(handSymbols[1]) == 4:
            type = 1
        else:
            type = 2
    elif len(handSymbols) == 3:
        if hand.count(handSymbols[0]) == 3 or hand.count(handSymbols[1]) == 3 or hand.count(handSymbols[2]) == 3:
            type = 3
        else:
            type = 4
    elif len(handSymbols) == 4:
        type = 5
    else:
        type = 6
    
    return type

class hand:
    def __init__(self, cards):
        self.cards = cards

    def __lt__(self, other):
        hand1 = self.cards
        hand2 = other.cards

        types = {hand1: 0, hand2: 0}
        for hand in [hand1, hand2]:
            best = bestHand(hand)
            types[hand] = handType(best)

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

symbols = 'AKQT98765432J'

cards = sorted(cards, key=lambda pair: pair[0], reverse=True)

s = 0

for i,pair in enumerate(cards):
    s += (i + 1) * pair[1]

print(s)
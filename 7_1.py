d = open("./input/ie.txt").read().split("\n")

vm = {
    "2": "a",
    "3": "b",
    "4": "c",
    "5": "d",
    "6": "e",
    "7": "f",
    "8": "g",
    "9": "h",
    "T": "i",
    "J": "j",
    "Q": "k",
    "K": "l",
    "A": "m",
}

class Hand:
    @classmethod
    def sort(cls, cards):
        return "".join([vm[v] for v in cards])

    def __init__(self, cards, mult, group=None):
        self.cards = cards
        self.srt = Hand.sort(cards)
        self.mult = int(mult)
        self.group = group

all_hands = [Hand(*r.split(" ")) for r in d]

groups = {}

def fullhouse(h):
    s = set(h)
    if len(s) == 2:
        s = "".join(s)
        return (h.count(s[0]) == 3 and h.count(s[1]) == 2) or (h.count(s[0]) == 2 and h.count(s[1]) == 3)
    return False

def four_of_a_kind(h):
    s = set(h)
    s = "".join(s)
    for c in s:
        if h.count(c) == 4:
            return True
    return False

def three_of_a_kind(h):
    s = set(h)
    if len(s) > 2:
        s = "".join(s)
        cnt = sorted([h.count(c) for c in s])
        return cnt == [1,1,3]
    return False

def two_pair(h):
    s = set(h)
    if len(s) == 3:
        o = sorted([h.count(v) for v in "".join(s)])
        return o == [1,2,2]
    return False

def one_pair(h):
    s = set(h)
    if len(s) == 4:
        o = sorted([h.count(v) for v in "".join(s)])
        return o == [1,1,1,2]
    return False


rules = [
    lambda x: True if len(set(x)) == 1 else False, # five-of-a-kind
    lambda x: four_of_a_kind(x),
    lambda x: fullhouse(x),
    lambda x: three_of_a_kind(x),
    lambda x: two_pair(x),
    lambda x: one_pair(x),
    lambda x: True if len(set(x)) == 5 else False
]

rules = rules[::-1]

# d = [('TTTTT', '1'), ('88884', '1'), ('23433', '1'), ('43533', '1'), ('43433', '1'), ('23456', '1'), ('44882', '1'), ('54882', '1'), ('34567', '1')]
# hands = [Hand(*r) for r in d]

for hand in all_hands:
    found = False
    for i, rule in enumerate(rules):
        if rule(hand.cards):
            hand.group = i
            found = True
            if i not in groups:
                groups[i] = [hand]
            else:
                groups[i].append(hand)
            break
    if not found:
        raise Exception(hand.cards)

sorted_hands = []

for i in sorted(groups.keys()):
    group, hands = i, groups[i]

    if len(hands) == 1:
        sorted_hands.append(hands[0])
    else:
        sh = sorted(hands, key=lambda c: c.srt)
        for hand in sh:
            sorted_hands.append(hand)

print([(h.group, h.cards) for h in sorted_hands])

results = []

for i, h in enumerate(sorted_hands):
    results.append(h.mult * (i+1))

print("Part 1: ", sum(results))
d = open("./input/i7.txt").read().split("\n")

vm = {
    "J": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "T": "j",
    "Q": "k",
    "K": "l",
    "A": "m",
}

class Hand:
    grouped_hands = {}
    group_map = {
        (1,1,1,1,1): 0,
        (1,1,1,2): 1,
        (1,2,2): 2,
        (1,1,3): 3,
        (2,3): 4,
        (1,4): 5,
        (5,): 6,
    }

    def solve(self):
        if "J" not in self.cards:
            s = set(self.cards)
            o = sorted([self.cards.count(v) for v in "".join(s)])
        else:
            jc = self.cards.count("J")
            s = set(self.cards.replace("J", ""))
            o = sorted([self.cards.count(v) for v in "".join(s)])
            print(self.cards, o, jc)
            try: 
                o[-1] += jc
            except:
                o = [jc]
        return Hand.group_map[tuple(o)]
        

    @classmethod
    def sort(cls, cards):
        return "".join([vm[v] for v in cards])

    def __init__(self, cards, mult):
        self.cards = cards
        self.srt = Hand.sort(cards)
        self.mult = int(mult)
        self.group = self.solve()

        if self.group not in Hand.grouped_hands:
            Hand.grouped_hands[self.group] = [self]
        else:
            Hand.grouped_hands[self.group].append(self)
    
    def __repr__(self) -> str:
        return f"Hand({self.cards}->{self.fingerprint})"

all_hands = [Hand(*r.split(" ")) for r in d]
# print(all_hands)

sorted_hands = []

for i in sorted(Hand.grouped_hands.keys()):
    group, hands = i, Hand.grouped_hands[i]

    if len(hands) == 1:
        sorted_hands.append(hands[0])
    else:
        sh = sorted(hands, key=lambda c: c.srt)
        for hand in sh:
            sorted_hands.append(hand)

# print([(h.group, h.cards) for h in sorted_hands])

results = []

for i, h in enumerate(sorted_hands):
    results.append(h.mult * (i+1))

print("Part 2: ", sum(results))
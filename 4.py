import math

d = [r for r in open("i4.txt").read().split("\n") if r]
games = []
pts = []
for g in d:
    w, c = g.split("|")
    w = w[w.index(":")+1:]
    w = set([w for w in w.split(" ") if w])
    c = set([c for c in c.split(" ") if c])
    games.append((w, c, 1))
    i = len(w.intersection(c))
    p = math.floor(2 ** (i - 1))
    pts.append(p)

print("part 1: ", sum(pts))

for i, g in enumerate(games):
    w, c, k = g
    s = len(w.intersection(c))
    for _ in range(k):
        for j in range(s):
            try:
                m = games[i + (1+j)]
                w, c, k = m
                games[i + (1+j)] = (w, c, k + 1)
            except:
                pass
    # print("round: ", i, [(g[0], g[1][2]) for g in enumerate(games)])

print("part 2: ", sum([g[2] for g in games]))
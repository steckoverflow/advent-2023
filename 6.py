from functools import reduce

d = [r.split() for r in open("./input/i6.txt").read().split("\n") if r]
tw = []

for t, r in zip([int(v) for v in d[0][1:]], [int(v) for v in d[1][1:]]):
    w = 0
    s = 0
    while s < t:
        td = (1 * s) * (t - (1 * s))
        if td > r:
            w += 1
        s += 1
    tw.append(w)


print("Part 1: ", reduce(lambda x, y: x * y, tw))

d = [r for r in open("./input/i6.txt").read().split("\n") if r]
t, r = int("".join(d[0].split()[1:])), int("".join(d[1].split()[1:]))

w = 0
s = 0
while s < t:
    td = (1 * s) * (t - (1 * s))
    if td > r:
        w += 1
    s += 1

print("Part 2: ", w)

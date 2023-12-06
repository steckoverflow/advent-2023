from datetime import datetime as dt

d = open("./input/i5.txt", "r").read().split("\n\n")
rs, *rmaps = d
s = tuple(int(s) for s in rs.split(" ") if s and s.isnumeric())
cmaps = []
lw = None

for m in rmaps:
    l = []
    for rn in (r for r in m[m.find(":") + 1 :].split("\n") if r):
        l.append(tuple(int(v) for v in rn.split(" ")))
    cmaps.append(tuple(l))


def smap(m, v):
    for rn in m:
        drs, srs, rl = rn
        if v >= srs and v < srs + rl:
            return drs + (v - srs)
    return v


for v in s:
    for mp in cmaps:
        v = smap(mp, v)
    if not lw or v < lw:
        lw = v

print("Part 1: ", lw)

ns = list(zip(s[::2], s[1::2]))  # sorted(, key=lambda x: x[0])
lw = None
lst = dt.now()
tc = 0

for si, j in ns:
    # print(si, j)
    for i in range(j):
        v = si + i

        for mp in cmaps:
            v = smap(mp, v)
        if not lw or v <= lw:
            lw = v

        if tc % 50_000_000 == 0:
            print(tc, dt.now() - lst, "lw: ", lw)

        tc += 1


print("Part 2: ", lw, "iterations: ", tc)

from datetime import datetime as dt

d = open("./input/ie.txt", "r").read().split("\n\n")
rs, *rmaps = d
s = tuple(int(s) for s in rs.split(" ") if s and s.isnumeric())
cmaps = []
lw = None

for m in rmaps:
    l = []
    for rn in (r for r in m[m.find(":")+1:].split("\n") if r):
        l.append(tuple(int(v) for v in rn.split(" ")))
    cmaps.append(tuple(l))  

def smap(m, v):
    for rn in m:
        drs, srs, rl = rn
        if v >= srs and v <= srs + rl:
            return drs + (v - srs)
    return v

for v in s:
    for mp in cmaps:
        v = smap(mp, v)
    if not lw or v < lw:
        lw = v

print("Part 1: ", lw)

ns = sorted(list(zip(s[::2], s[1::2])), key=lambda x: x[0])
lw = None
lst = dt.now()

for si, j in ns:
    for i in range(j):
        v = si + i
        if i % 10_000_000 == 0:
            print(i, dt.now() - lst)
        for mp in cmaps:
            v = smap(mp, v)
        if not lw or v < lw:
            lw = v

print("Part 2: ", lw)

# print(ns)

# maps = maps[::-1]

# def reverse_loop(m):
#     l = [[int(v) for v in v.split(" ")] for v in [r for r in m[m.find(":")+1:].split("\n") if r]]
#     l = sorted(l, key=lambda x: x[0])
#     for rn in l:
#         for i in range(rn[2]):
#             yield rn[0] + i

# numbers = reverse_loop(maps[0])
# found = False

# for i in numbers:
#     if found: 
#         break
#     if i == 46:
#         print(i)
#     if i % 1_000_000 == 0:
#         print(i)
#     for m in maps:
#         for mp in maps:
#             sd = smap(mp, sd)
#     for rn in ns:
#         si, j = rn
#         if sd >= si and sd <= si + j - 1:
#             print("Part 2: ", sd)
#             found = True
#             break


# counter = 0

# for rn in ns:
#     si, j = rn
#     for i in range(j):
#         counter += 1
#         if counter % 100000 == 0:
#             print(counter)
#         sd = si + i
#         for mp in maps:
#             sd = smap(mp, sd)
#         if not lw or sd < lw:
#             lw = sd

# print("Part 2: ", lw)



# ns = [(n[0], n[0]+ n[1] - 1) for n in ns]
# l = {0: ns}

# for i in range(len(maps)):
#     orn = l[i]
#     l[i+1] = []

#     for rn in orn:
#         ss, se = rn
#         ss2 = smap(maps[i], ss)
#         while not ss2 and ss <= se + 1:
#             ss +=1
#             ss2 = smap(maps[i], ss)
#             if ss==se:
#                 l[i+1].append(rn)
#                 break
#         if ss2:
#             l[i+1].append((ss2, se + ss2 - ss))
# print(ns)




# # l = {0: ns}

# # def smap2(m, v):
# #     for rn in (r for r in m[m.find(":")+1:].split("\n") if r):
# #         drs, srs, rl = (int(v) for v in rn.split(" "))
# #         if v >= srs and v <= srs + rl:
# #             return drs + (v - srs), srs + rl

# # for i in range(len(maps)):
# #     orn = l[i]
# #     l[i+1] = []

# #     for rn in orn:
# #         ss, se = rn
# #         ss2 = smap2(maps[i], ss)
# #         while not ss2 and ss <= se + 1:
# #             ss +=1
# #             ss2 = smap2(maps[i], ss)
# #             if ss==se:
# #                 l[i+1].append(rn)
# #                 break
# #         if ss2:
# #             l[i+1].append((ss2[0], se + ss2[0] - ss))

# #     # for varje range i vår level ()

# # print(l)


# # ranges = {}

# # def generate_ranges(m, r=None):
# #     if not r:
# #         r = {}
# #     for i, rn in enumerate((r for r in m[m.find(":")+1:].split("\n") if r)):
# #         drs, srs, rl = (int(v) for v in rn.split(" "))
# #         r[i] = srs, srs + rl - 1
# #     return r

# # for i, mp in enumerate(maps):
# #     ranges[i] = generate_ranges(mp)

# # print(ranges)







# # s = [int(s) for s in s[s.find(":")+1:].split() if s]
# # lw = None

# # maps = maps[::-1]

# # ns = maps[0]

# # # 60 56 37
# # # 56 93 4


# # print(s, ns)

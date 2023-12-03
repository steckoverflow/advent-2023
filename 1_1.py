d = open("i1.txt").read().split("\n")
print(d)

s = []

for r in d:
    v = ""
    for c in r:
        try:
            int(c)
            v += c
            break
        except:
            continue
    for c in r[::-1]:
        try:
            int(c)
            v += c
            break
        except:
            continue
    if v:
        s.append(int(v))

print(sum(s))
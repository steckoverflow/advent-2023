import pprint

d = [list(r) for r in open("i3.txt").read().split("\n") if r]
s = []
symbols = ('*', '$', '/', '+', '=', '#','@', '%', '&', '-')
number_positions = []

for i in range(len(d)):
    n = ""
    si = None
    for j in range(len(d[i]) + 1):
        try:
            c = d[i][j]
            int(c)
            n += c
            if not si:
                si = (i, j)
        except:
            if n:
                number_positions.append((int(n), (si, (si[0], si[1] + len(n) - 1))))
                i = si[0]
                for j in range(si[1], si[1] + len(n)):
                    if i > 0:
                        v = d[i-1][j] 
                        if v in symbols:
                            s.append(int(n))
                            break
                    
                    if i + 1 < len(d):
                        v = d[i+1][j]
                        if v in symbols:
                            s.append(int(n))
                            break
                    
                    if j - 1 > 0 and j == si[1]:
                        v = d[i][j-1] 
                        if v in symbols:
                            s.append(int(n))
                            break

                    if i  > 0 and j > 0:
                        v = d[i-1][j-1] 
                        if v in symbols:
                            s.append(int(n))
                            break

                    if i + 1 < len(d):
                        v = d[i+1][j-1] 
                        if v in symbols:
                            s.append(int(n))
                            break

                    if j + 1 < len(d[0]) and j == si[1] + len(n) - 1:
                        v = d[i][j+1] 
                        if v in symbols:
                            s.append(int(n))
                            break

                    if i  > 0 and j + 1 < len(d[0]):
                        v = d[i-1][j+1] 
                        if v in symbols:
                            s.append(int(n))
                            break

                    if i + 1 < len(d) and j + 1 < len(d[0]):
                        v = d[i+1][j+1] 
                        if v in symbols:
                            s.append(int(n))
                            break
            n = ""
            si = None
            continue

print("part 1: ", sum(s))

gear_positions = []

for i in range(len(d)):
    for j in range(len(d[i])):
        if d[i][j] == '*':
            gear_positions.append((i, j))

s2 = []

for pos in gear_positions:
    nums = []
    i, j = pos
    for np in number_positions:
        n, p = np
        if abs(p[0][0] - i) <= 1:
            lct = abs(p[0][1] - j)
            rct = abs(p[1][1] - j)
            if lct <= 1 or rct <= 1:
                nums.append(n)
    if len(nums) == 2:
        s2.append(nums[0] * nums[1])

print("part 2: ", sum(s2))


    

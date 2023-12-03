d = [r for r in open("i1.txt").read().split("\n") if r]
s = []

def loop(r, reverse=False):
    if reverse:
        r = r[::-1]

    for i in range(len(r)):
        c = r[i]
        if c.isnumeric():
            return c 
        
        if not reverse:
            if r[i:i+3] == 'one':
                return "1"
            elif r[i:i+3] == 'two':
                return "2"
            elif r[i:i+3] == 'six':
                return "6"
            elif r[i:i+4] == 'four':
                return "4"
            elif r[i:i+4] == 'five':
                return "5"
            elif r[i:i+4] == 'nine':
                return "9"
            elif r[i:i+5] == 'three':
                return "3"
            elif r[i:i+5] == 'seven':
                return "7"
            elif r[i:i+5] == 'eight':
                return "8"
        else:
            if r[i:i+3] == 'eno':
                return "1"
            elif r[i:i+3] == 'owt':
                return "2"
            elif r[i:i+3] == 'xis':
                return "6"
            elif r[i:i+4] == 'ruof':
                return "4"
            elif r[i:i+4] == 'evif':
                return "5"
            elif r[i:i+4] == 'enin':
                return "9"
            elif r[i:i+5] == 'eerht':
                return "3"
            elif r[i:i+5] == 'neves':
                return "7"
            elif r[i:i+5] == 'thgie':
                return "8"

for r in d:
    v = ""
    v += loop(r)
    v += loop(r, True)
    if v:
        s.append(int(v))

print(s)
print(sum(s))
from functools import reduce

rgb = {"red": 12, "green": 13, "blue": 14}
impossible = []
products = []
data = [{int(r.split(":")[0].replace("Game ", "")): r.split(":")[1].split(";")} for r in open("i2.txt").read().split("\n") if r]
for game in data:
    mxvs = {}
    for gi, gv in game.items():
        for draw in gv:
            for cubes in draw.split(","):
                cv = rgb[cubes.strip().split(" ")[1]]
                v = int(cubes.strip().split(" ")[0])
                if cubes.strip().split(" ")[1] not in mxvs or v > mxvs[cubes.strip().split(" ")[1]]:
                    mxvs[cubes.strip().split(" ")[1]] = v
                if (v > cv):
                    if gi not in impossible:
                        impossible.append(gi)
    products.append(reduce(lambda x, y: x * y, mxvs.values()))

print("1: ", sum([i for i in range(1, 101) if i not in impossible]))
print("2: ", sum(products))
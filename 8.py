from collections import OrderedDict
from math import lcm

d = open("./input/i8.txt", "r").read().split("\n\n")
ins = d[0]
mv = d[1].split("\n")
g = OrderedDict()
lrm = {"L": 0, "R": 1}

for m in mv:
    v, d = [v.strip() for v in m.split("=")]
    d1, d2 = [v.strip().replace("(", "").replace(")", "") for v in d.split(",")]
    g[v] = (d1, d2)

steps = 0
last_node = "AAA"

while last_node != "ZZZ":
    i = steps % len(ins)
    c = ins[i]
    last_node = g[last_node][lrm[c]]
    steps += 1

print("Part 1: ", steps)

steps = 0
last_nodes = [n for n in g.keys() if n[-1] == "A"]
last_nodes_solved = {i: [] for i in range(len(last_nodes))}
target = lambda n: n[-1] == "Z"

while not all([len(v) > 1 for v in last_nodes_solved.values()]):
    j = steps % len(ins)
    c = ins[j]
    for i, n in enumerate(last_nodes):
        nn = g[n][lrm[c]]
        last_nodes[i] = nn
        if target(nn):
            if len(last_nodes_solved[i]) < 2:
                last_nodes_solved[i].append(steps)
    steps += 1

last_nodes_solved_diff = {
    i: last_nodes_solved[i][1] - last_nodes_solved[i][0]
    for i in range(len(last_nodes_solved))
}

print("Part 2: ", lcm(*last_nodes_solved_diff.values()))

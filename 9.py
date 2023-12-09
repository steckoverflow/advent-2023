d = [v.split() for v in open("./input/i9.txt").read().split("\n")]

class Seq:
    def __init__(self, seq, reverse=False):
        self.seq = [list(map(lambda x: int(x), seq))]
        self.calc_diff()
        self.s = self.solve(reverse)
    
    def solve(self, reverse):
        for i in range(-1, -len(self.seq) -1, -1):
            if i == -1:
                self.seq[i].insert(0, 0)
                continue
            ip = len(self.seq[i]) if not reverse else 0
            if reverse:
                v = self.seq[i][0] - self.seq[i+1][0]
            else:
                v = self.seq[i+1][-1] + self.seq[i][-1]
            self.seq[i].insert(ip, v)

        return self.seq[0][0] if reverse else self.seq[0][-1]

    def calc_diff(self):
        while not all([i == 0 for i in self.seq[-1]]):
            self.seq.append([self.seq[-1][i+1] - self.seq[-1][i] for i in range(len(self.seq[-1]) - 1)])

    def __repr__(self):
        return str(self.seq)

s = [Seq(v) for v in d]

print("Part 1: ", sum(list(map(lambda x: x.s, s))))

s = [Seq(v, reverse=True) for v in d]

print("Part 1: ", sum(list(map(lambda x: x.s, s))))
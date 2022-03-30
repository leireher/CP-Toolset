class UnionFindDisjointSet:
    def __init__(self, n: int):
        self.p = [-1 for _ in range(n)]
        self.set_size = [1 for _ in range(n)]
        self.n = n

    def find_set(self, i: int):
        if self.p[i] < 0:
            return i

        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i: int, j: int):
        return self.find_set(i) == self.find_set(j)

    def set_amount(self):
        return self.n

    def set_size(self, i: int):
        return self.set_size[self.find_set(i)]

    def union_set(self, i: int, j: int):
        if self.is_same_set(i, j):
            return

        self.n -= 1
        x, y = self.find_set(i), self.find_set(j)

        if self.p[x] < self.p[y]:  # rank[x] > rank[y]
            self.p[y] = x
            self.set_size[x] += self.set_size[y]
        else:
            self.p[x] = y
            self.set_size[y] += self.set_size[x]
            if self.p[x] == self.p[y]:
                self.p[y] -= 1

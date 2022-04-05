def LSOne(s):
    return s & -s


class FenwickTree:
    def __init__(self, n):
        self.ft = [0 for _ in range(n + 1)]

    def rsq(self, b):
        sum = 0
        while b > 0:
            sum += self.ft[b]
            b -= LSOne(b)
        return sum

    def rsq(self, a, b):
        return self.rsq(b) - (0 if a == 1 else self.rsq(a - 1))

    def adjust(self, k, v):
        while k < len(self.ft):
            self.ft[k] += v
            k += LSOne(k)

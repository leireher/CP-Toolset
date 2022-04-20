def LSOne(s):
    return s & -s


# Queries for dynamic RSQ in O(log n), elements numbered from 1 to n
class FenwickTree:
    def __init__(self, n):
        self.ft = [0 for _ in range(n + 1)]

    def get_sum(self, a):
        sum = 0
        while a > 0:
            sum += self.ft[a]
            a -= LSOne(a)
        return sum

    def get_range_sum(self, a, b):
        return self.get_sum(b) - (0 if a == 1 else self.get_sum(a - 1))

    def adjust(self, k, v):
        while k <= len(self.ft):
            self.ft[k] += v
            k += LSOne(k)

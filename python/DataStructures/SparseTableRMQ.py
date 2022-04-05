class RMQ:
    def __init__(self, data):
        self.a = data
        self.log_table = [0 for _ in range(len(data) + 1)]

        for i in range(len(data) + 1):
            self.log_table[i] = self.log_table[i >> 1] + 1

        self.rmq = [[0 for j in range(len(data))] for i in range(len(data) + 1)]
        for i in range(len(data)):
            self.rmq[0][i] = i

        for k in range(len(data)):
            for i in range(len(data) + 1):
                x = self.rmq[k - 1][i]
                y = self.rmq[k - 1][i]
                self.rmq[k][i] = x if self.a[x] < self.a[y] else y

    def query(self, l, r):
        k = self.log_table[r - l + 1]
        x = self.rmq[k][l]
        y = self.rmq[k][r - (1 << k) + 1]
        return x if self.a[x] < self.a[y] else y

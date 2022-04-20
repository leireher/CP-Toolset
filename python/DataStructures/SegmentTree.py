import sys
import math
sys.setrecursionlimit(10**7)

class SegmentTree():
    DEFAULT = {
        'min': 1 << 60,
        'max': -(1 << 60),
        'sum': 0,
        'prd': 1,
        'gcd': 0,
        'lmc': 1,
        '^': 0,
        '&': (1 << 60) - 1,
        '|': 0,
    }

    FUNC = {
        'min': min,
        'max': max,
        'sum': (lambda x, y: x + y),
        'prd': (lambda x, y: x * y),
        'gcd': math.gcd,
        'lmc': (lambda x, y: (x * y) // math.gcd(x, y)),
        '^': (lambda x, y: x ^ y),
        '&': (lambda x, y: x & y),
        '|': (lambda x, y: x | y),
    }

    def __init__(self, N, ls, mode='min'):
        """
Number of leaves N,Element ls,Function mode(min,max,sum,prd(product),gcd,lmc,^,&,|)
        """
        self.default = self.DEFAULT[mode]
        self.func = self.FUNC[mode]
        self.N = N
        self.K = (N - 1).bit_length()
        self.N2 = 1 << self.K
        self.dat = [self.default] * (2**(self.K + 1))
        for i in range(self.N):  #Leaf construction
            self.dat[self.N2 + i] = ls[i]
        self.build()

    def build(self):
        for j in range(self.N2 - 1, -1, -1):
            self.dat[j] = self.func(self.dat[j << 1], self.dat[j << 1 | 1])  #Conditions that parents have

    def leafvalue(self, x):  #The xth value in the list
        return self.dat[x + self.N2]

    def update(self, x, y):  # index(x)To y
        i = x + self.N2
        self.dat[i] = y
        while i > 0:  #Change parent value
            i >>= 1
            self.dat[i] = self.func(self.dat[i << 1], self.dat[i << 1 | 1])
        return

    def query(self, L, R):  # [L,R)Section acquisition
        L += self.N2
        R += self.N2
        vL = self.default
        vR = self.default
        while L < R:
            if L & 1:
                vL = self.func(vL, self.dat[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.dat[R], vR)
            L >>= 1
            R >>= 1
        return self.func(vL, vR)

# Two-phase simplex algorithm for solving linear programs of the form
#     maximize     c^T x
#     subject to   Ax <= b
#                  x >= 0
# INPUT: A -- an m x n matrix
#        b -- an m-dimensional vector
#        c -- an n-dimensional vector
# OUTPUT: value of the optimal solution (infinity if unbounded
#         above, nan if infeasible), and a vector where the optimal 
#         solution will be stored
# To use this code, create an LPSolver object with A, b, and c as
# arguments.  Then, call Solve().

EPS = 1e-9

class LPSolver:
    def __init__(self, a, b, c):
        self.m = len(b)
        self.n = len(c)
        self.N = [0 for _ in range(self.n + 1)]
        self.B = [0 for _ in range(self.m)]
        self.D = [[.0 for x in range(self.n + 2)] for y in range(self.m + 2)]
        for i in range(self.m):
            for j in range(self.n):
                self.D[i][j] = a[i][j]

        for i in range(self.m):
            self.B[i] = self.n + 1
            self.D[i][self.n] = -1
            self.D[i][self.n + 1] = b[i]

        for j in range(self.n):
            self.N[j] = j
            self.D[self.m][j] = -c[j]

        self.N[self.n], self.D[self.m + 1][self.n] = -1, 1

    def pivot(self, r, s):
        for i in range(self.m + 2):
            if i != r:
                for j in range(self.n + 2):
                    if j != s:
                        self.D[i][j] -= self.D[r][j] * self.D[i][s] / self.D[r][s]
                        
        for j in range(self.n + 2):
            if j != s:
                self.D[r][j] /= self.D[r][s]

        for i in range(self.m + 2):
            if i != r:
                self.D[i][s] /= -self.D[r][s]

        self.D[r][s] = 1.0 / self.D[r][s]
        self.B[r], self.N[s] = self.N[s], self.B[r]

    def simplex(self, phase):
        x = self.m + 1 if phase == 1 else self.m
        while True:
            s = -1
            for j in range(self.n + 1):
                if phase == 2 and self.N[j] == -1:
                    continue
                if s == -1 or self.D[x][j] < self.D[x][s] or self.D[x][j] == self.D[x][s] and self.N[j] < self.N[s]:
                    s = j

            if self.D[x][s] >= -EPS:
                return True

            r = -1
            for i in range(self.m):
                if self.D[i][s] <= 0:
                    continue
                if r == -1 or (self.D[i][self.n + 1] / self.D[i][s]) < (self.D[r][self.n + 1] / self.D[r][s]) or (self.D[i][self.n + 1] / self.D[i][s] == self.D[r][self.n + 1] / self.D[r][s]) and self.B[i] < self.B[r]:
                    r = i

            if r == -1:
                return False

            self.pivot(r, s)

    def solve(self):
        r = 0
        for i in range(1, self.m):
            if self.D[i][self.n + 1] < self.D[r][self.n + 1]:
                r = i
        if self.D[r][self.n + 1] <= -EPS:
            self.pivot(r, self.n)
            if not self.simplex(1) or self.D[self.m + 1][self.n + 1] < -EPS:
                return -float("inf")
            
            for i in range(self.m):
                if self.B[i] == -1:
                    s = -1
                    for j in range(self.n + 1):
                        if s == -1 or self.D[i][j] < self.D[i][s] or self.D[i][j] == self.D[i][s] and self.N[j] < self.N[s]:
                            s = j
                    self.pivot(i, s)

        if not self.simplex(2):
            return float("inf")

        x = [0. for _ in range(self.n)]
        for i in range(self.m):
            if self.B[i] < self.n:
                x[self.B[i]] = self.D[i][self.n + 1]

        return self.D[self.m][self.n + 1], x

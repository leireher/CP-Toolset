from numbers import Number
from copy import deepcopy

INF = float('inf')

#USAGE
#Create MaxFlow(V) and add edges to graph using add_edge(u,v,w).
#Use dinic(s,t) to find max flow from s to t.
class MaxFlow:
    def __init__(self, V: int):
        self.V = V
        self.EL = []
        self.AL = [list() for _ in range(self.V)]
        self.d = []
        self.last = []
        self.p = []

    def BFS(self, s: int, t: int) -> bool:
        self.d = [-1] * self.V
        self.d[s] = 0
        self.p = [[-1, -1] for _ in range(self.V)]
        q = [s]
        while len(q) != 0:
            u = q[0]
            q.pop(0)
            if u == t:
                break
            for idx in self.AL[u]:
                v, cap, flow = self.EL[idx]
                if cap - flow > 0 and self.d[v] == -1:
                    self.d[v] = self.d[u]+1
                    q.append(v)
                    self.p[v] = [u, idx]
        return self.d[t] != -1

    def DFS(self, u: int, t: int, f: Number = INF) -> Number:
        if u == t or f == 0:
            return f
        for i in range(self.last[u], len(self.AL[u])):
            self.last[u] = i
            v, cap, flow = self.EL[self.AL[u][i]]
            if self.d[v] != self.d[u]+1:
                continue
            pushed = self.DFS(v, t, min(f, cap - flow))
            if pushed != 0:
                flow += pushed
                self.EL[self.AL[u][i]][2] = flow
                self.EL[self.AL[u][i] ^ 1][2] -= pushed
                return pushed
        return 0

    #Default directed edge
    def add_edge(self, u: int, v: int, capacity: Number,
                 directed: bool = True) -> None:
        if u == v:
            return
        self.EL.append([v, capacity, 0])
        self.AL[u].append(len(self.EL)-1)
        self.EL.append([u, 0 if directed else capacity, 0])
        self.AL[v].append(len(self.EL)-1)

    #Max flow
    def dinic(self, s: int, t: int) -> Number:

        mf = 0
        while self.BFS(s, t):
            self.last = [0] * self.V
            f = self.DFS(s, t)
            while f != 0:
                mf += f
                f = self.DFS(s, t)
        return mf

    #Copy the object (avoid destroying instance)
    def copy(self) -> 'MaxFlow':
        return deepcopy(self)

#INCREASE RECURSION
#sys.setrecursionlimit(100000)

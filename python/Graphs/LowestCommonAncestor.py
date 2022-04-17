#USAGE
#Create LCA object for the given adjacency list
#Use find(u,v) to find LCA of nodes u and v
#REQUIRES RMQ IMPLEMENTATION
#Par[i] = parent of node i in the DFS, root is its own parent
#E[i] = i-th node visited in the DFS (Euler tour)
#L[i] = levels of the i-th node visited in the DFS (Euler tour)
#H[i] = index of the first occurrence of node i in E
class LCA:

    def __init__(self, V, AL):
        self.idx = 0
        self.AL = AL
        self.V = V
        self.Par = [-1 for _ in range(V)]
        self.E = [None for _ in range(2*V-1)]
        self.L = [None for _ in range(2*V-1)]
        self.H = [-1 for _ in range(V)]
        self.dfs(0,0,0)
        self.rmq = RMQ(self.L)

    def dfs(self,cur, depth, parent):
        self.Par[cur] = parent
        self.H[cur] = self.idx
        self.E[self.idx] = cur
        self.L[self.idx] = depth
        self.idx += 1
        for i in range(len(self.AL[cur])):
            if (self.Par[self.AL[cur][i]] == -1):
                self.dfs(self.AL[cur][i], depth + 1, cur)
                self.E[self.idx] = cur
                self.L[self.idx] = depth
                self.idx += 1

    def depth(self,u):
        return self.L[self.H[u]]

    def parent(self,u):
        return self.Par[u]

    def find(self,u,v):
        if (self.H[u] > self.H[v]):
            u,v = v,u
        return self.E[self.rmq.query(self.H[u], self.H[v])]

#INCREASE RECURSION
#sys.setrecursionlimit(100000)

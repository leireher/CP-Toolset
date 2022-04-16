dfsNumberCounter = 0
numSCC = 0
dfs_num = []
dfs_low = []
S = []
visited = []
st = []
nodesSCC = []

# dfs_num[i] = orden en el que se visita por primera vez el nodo i */
# dfs_low[i] = minimo num alcanzable desde el nodo i y desde sus hijos en la busqueda */
# st = Pila que guarda los nodos según el orden en que se exploran */
# Inicializar 'dfsNumberCounter' y 'numSCC' a 0 antes de llamar a la función */
# 'nodesSCC' guarda los componentes fuertemente conexos (SON DISJUNTOS)
def tarjanSCC(AL,u):
  global dfs_low, dfs_num, dfsNumberCounter, visited
  global numSCC, st, nodesSCC

  dfs_low[u] = dfs_num[u] = dfsNumberCounter
  dfsNumberCounter += 1
  st.append(u)
  visited[u] = True
  for v, w in AL[u]:
    if dfs_num[v] == -1:
      tarjanSCC(AL,v)
    if visited[v]:
      dfs_low[u] = min(dfs_low[u], dfs_low[v])

  if dfs_low[u] == dfs_num[u]:
    numSCC += 1
    while True:
      v = st[-1]
      st.pop()
      visited[v] = False
      nodesSCC[numSCC-1].append(v)
      if u == v:
        break

def SCC(AL,V):
  global dfs_low, dfs_num, dfsNumberCounter, visited
  global numSCC, st, nodesSCC
  dfs_num = [-1] * V
  dfs_low = [0] * V
  visited = [False] * V
  nodesSCC = [[] for _ in range(V)]
  st = []
  numSCC = 0
  dfsNumberCounter = 0
  for u in range(V):
      if dfs_num[u] == -1:
        tarjanSCC(AL,u)

#INCREASE RECURSION LIMIT!
#sys.setrecursionlimit(100000)

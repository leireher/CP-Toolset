dfs_num = []
dfs_low = []
dfs_parent = []
articulation_vertex = []
dfsNumberCounter = 0
dfsRoot = 0
rootChildren = 0

# dfs_num[i] = orden en el que se visita por primera vez el nodo i
# dfs_low[i] = mínimo num alcanzable desde el nodo i y desde sus hijos en la búsqueda
# Establecer 'dfsRoot' al nodo raíz de la búsqueda, y 'rootChildren' y 'dfsNumberCounter' a 0 antes de llamar a
# articulationPointAndBridge(AL,root)
# Al -> Adjacency list
def articulationPointAndBridge(AL,u):
  global dfs_num, dfs_parent, dfs_low, articulation_vertex
  global dfsNumberCounter, dfsRoot, rootChildren

  dfs_low[u] = dfs_num[u] = dfsNumberCounter
  dfsNumberCounter += 1
  for (v, w) in AL[u]:
    if dfs_num[v] == -1:
      dfs_parent[v] = u
      if u == dfsRoot:
        rootChildren += 1

      articulationPointAndBridge(AL,v)

      if dfs_low[v] >= dfs_num[u]:
        articulation_vertex[u] = True
      if dfs_low[v] > dfs_num[u]:
        print(' Edge (%d, %d) is a bridge' % (u, v))
      dfs_low[u] = min(dfs_low[u], dfs_low[v])
    elif v != dfs_parent[u]:
      dfs_low[u] = min(dfs_low[u], dfs_num[v])

# Articulation -> Nodo que tras ser eliminado divide el componente conexo
# Bridge -> Arista entre u y v que tras ser eliminada hace que no haya camino entre u y v
def findArtBrid(AL, V):
  global dfs_num, dfs_parent, dfs_low, articulation_vertex
  global dfsNumberCounter, dfsRoot, rootChildren

  print('Articulation Points & Bridges (the input graph must be UNDIRECTED)')
  dfs_num = [-1] * V
  dfs_low = [0] * V
  dfs_parent = [-1] * V
  articulation_vertex = [False] * V
  dfsNumberCounter = 0
  print('Bridges:')
  for u in range(V):
    if dfs_num[u] == -1:
      dfsRoot = u
      rootChildren = 0
      articulationPointAndBridge(AL,u)
      articulation_vertex[dfsRoot] = (rootChildren > 1)

  print('Articulation Points:')
  for u in range(V):
    if articulation_vertex[u]:
      print(' Vertex %d' % u)

#INCREASE RECURSION LIMIT!
#sys.setrecursionlimit(100000)

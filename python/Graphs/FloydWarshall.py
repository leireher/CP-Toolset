# COMPLEXITY: O(V^3) (V < 400)
# adj_mat = matriz de adyacencia del grafo
# adj_mat[i][j] = INF si no hay arista
# adj_mat[i][i] = 0
# V = cantidad de nodos
# Si despues de todo la diagonal tiene un valor menor que cero, tiene ciclos negativos
def floyd_warshall(AM,V):
	for k in range(V):	# loop order is k->u->v
		for u in range(V):
			for v in range(V):
				AM[u][v] = min(AM[u][v], AM[u][k] + AM[k][v])

	for u in range(V):
		for v in range(V):
			print("APSP({}, {}) = {}".format(u, v, AM[u][v]))

from heapq import heappush, heappop

# AL -> Adjacency list
# COMPLEXITY: O((V+E)log V) (V,E < 300K)
def dijkstra(AL,V,s):
    INF = int(1e9)

    # (Modified) Dijkstra's routine
    dist = [INF for u in range(V)]
    dist[s] = 0
    pq = []
    heappush(pq, (0, s))

    # sort the pairs by non-decreasing distance from s
    while (len(pq) > 0):                    # main loop
        d, u = heappop(pq)                  # shortest unvisited u
        if (d > dist[u]): continue          # a very important check
        for v, w in AL[u]:                  # all edges from u
            if (dist[u]+w >= dist[v]): continue # not improving, skip
            dist[v] = dist[u]+w             # relax operation
            heappush(pq, (dist[v], v))  

    for u in range(V):
        print("SSSP({}, {}) = {}".format(s, u, dist[u]))

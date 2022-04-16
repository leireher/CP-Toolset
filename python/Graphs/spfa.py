from collections import deque

# Shortest Path Faster Algorithm
# SSSP adjacency-list implementation that handles negative weight cycles.
# The function returns true if such a cycle is detected (i.e., it can be reached from s).
# If not, dist[i] = distance from source node s to node i.
# Worst-case complexity: O(VE), in practice better than Bellman-Ford, but not than Dijkstra.
def SPFA(AL,V,s):
    INF = int(1e9)

    # SPFA from source S
    # initially, only source vertex s has dist[s] = 0 and in the queue
    dist = [INF for u in range(V)]
    dist[s] = 0
    q = deque()
    q.append(s)
    in_queue = [0 for u in range(V)]
    veces = [0 for u in range(V)]
    in_queue[s] = 1
    veces[s] = 1
    while (len(q) > 0):
        u = q.popleft()                          # pop from queue
        in_queue[u] = 0
        for v, w in AL[u]:
            if (dist[u]+w >= dist[v]): continue  # not improving, skip
            dist[v] = dist[u]+w                  # relax operation
            if not in_queue[v]:                  # add to the queue
                q.append(v)                      # only if v is not
                in_queue[v] = 1                  # already in the queue
                veces[v] += 1
                #Negative cycle
                if(veces[v]==V):
                    return True

    for u in range(V):
        print("SSSP({}, {}) = {}".format(s, u, dist[u]))

    return False

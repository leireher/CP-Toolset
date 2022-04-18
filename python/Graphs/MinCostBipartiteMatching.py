# Min cost bipartite matching via shortest augmenting paths
#
# This is an O(n^3) implementation of a shortest augmenting path
# algorithm for finding min cost perfect matchings in dense
# graphs. Note that both partitions must be of equal size!!
# (IF NOT EQUAL SIZE, ADD FAKE VERTICES AND EDGES THAT DON'T
# MODIFY THE ANSWER (0.0 costs))
#
#   cost[i][j] = cost for pairing left node i with right node j
#   Lmate[i] = index of right node that left node i pairs with
#   Rmate[j] = index of left node that right node j pairs with
#
# The values in cost[i][j] may be positive or negative.  To perform
# maximization, simply negate the cost[][] matrix.

def MinCostMatching(cost):
    n = len(cost);
    # construct dual feasible solution
    u = [None] * n
    v = [None] * n
    for i in range(n):
        u[i] = cost[i][0]
        for j in range(1,n):
            u[i] = min(u[i], cost[i][j])
    for j in range(n):
        v[j] = cost[0][j] - u[0]
        for i in range(1,n):
            v[j] = min(v[j], cost[i][j] - u[i])
    # construct primal solution satisfying complementary slackness
    Lmate = [-1]*n
    Rmate = [-1]*n
    mated = 0
    for i in range(n):
        for j in range(n):
            if (Rmate[j] != -1):
                continue
            if (abs(cost[i][j] - u[i] - v[j]) < 10**(-10)):
                Lmate[i] = j
                Rmate[j] = i
                mated += 1
                break

    dist = [None] * n
    # repeat until primal solution is feasible
    while (mated < n):
        # find an unmatched left node
        s = 0
        while (Lmate[s] != -1):
            s += 1
        # initialize Dijkstra

        dad = [-1] * n
        seen = [0] * n
        for k in range(n):
            dist[k] = cost[s][k] - u[s] - v[k]

        j = 0;
        while (True):
            # find closest
            j = -1;
            for k in range(n):
                if (seen[k]):
                    continue
                if (j == -1 or dist[k] < dist[j]):
                    j = k
            seen[j] = 1
            # termination condition
            if (Rmate[j] == -1):
                break
            # relax neighbors
            i = Rmate[j]
            for k in range(n):
                if (seen[k]):
                    continue
                new_dist = dist[j] + cost[i][k] - u[i] - v[k]
                if (dist[k] > new_dist):
                    dist[k] = new_dist
                    dad[k] = j
        # update dual variables
        for k in range(n):
            if (k == j or not seen[k]):
                continue
            i = Rmate[k]
            v[k] += dist[k] - dist[j]
            u[i] -= dist[k] - dist[j]
        u[s] += dist[j]
        # augment along path
        while (dad[j] >= 0):
            d = dad[j]
            Rmate[j] = Rmate[d]
            Lmate[Rmate[j]] = j
            j = d
        Rmate[j] = s
        Lmate[s] = j
        mated += 1
    value = 0
    for i in range(n):
        value += cost[i][Lmate[i]]
    return value

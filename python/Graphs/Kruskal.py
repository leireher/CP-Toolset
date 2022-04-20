from heapq import heappush, heappop

#EL -> Edge list
# COMPLEXITY: O(E log E)
def kruskal(EL,V,E):
    EL.sort()                                       # sort by w, O(E log E)

    mst_cost = 0
    num_taken = 0
    UF = UnionFindDisjointSet(V)                    # all V are disjoint sets

    for i in range(E):                              # for each edge, O(E)
        if num_taken == V-1:
            break
        w, u, v = EL[i]
        if (not UF.is_same_set(u, v)):                # check
            num_taken += 1                          # 1 more edge is taken
            mst_cost += w                           # add w of this edge
            UF.union_set(u, v)                       # link them
            # note: the runtime cost of UFDS is very light

    # note: the number of disjoint sets must eventually be 1 for a valid MST
    print("MST cost = {} (Kruskal's)".format(mst_cost))

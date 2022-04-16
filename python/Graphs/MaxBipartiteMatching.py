import random

match = []
vis = []

# Maximum Cardinality Bipartite Matching
# También es útil para:
#   Maximum Independent Set = |V| - MCBM
#	Minimum Vertex Cover = MCBM
def Aug(AL,L):
    global match, vis

    if vis[L]:
        return 0
    vis[L] = 1
    for R in AL[L]:
        if match[R] == -1 or Aug(AL,match[R]):
            match[R] = L
            return 1
    return 0

def matching(AL,V,Vleft):
    global match, vis

    freeV = set()
    for L in range(Vleft):
        freeV.add(L)
    match = [-1] * V
    MCBM = 0

    for L in range(Vleft):
        candidates = []
        for R in AL[L]:
            if match[R] == -1:
                candidates.append(R)
        if len(candidates) > 0:
            MCBM += 1
            freeV.remove(L)
            a = random.randrange(len(candidates))
            match[candidates[a]] = L
 
    for f in freeV:
        vis = [0] * Vleft
        MCBM += Aug(AL,f)

    print('Found %d matchings' % MCBM)

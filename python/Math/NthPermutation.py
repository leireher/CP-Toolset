# e The number of entries
# n The index of the permutation
def nthPermutation(e, n):
    j, k = 0, 1
    fact = [0 for _ in range(e)]
    perm = [0 for _ in range(e)]
    fact[0] = 1
    
    # compute factorial numbers
    while k < e:
        fact[k] = fact[k - 1] * k
        k += 1

    # compute factorial code
    for k in range(e):
        perm[k] = n // fact[e - 1 - k]
        n = n % fact[e - 1 - k]

    # readjust values to obtain the permutation
    # start from the end and check if preceding values are lower
    for k in reversed(range(e)):
        for j in reversed(range(k)):
            if perm[j] <= perm[k]:
                perm[k] += 1

    # perm[0..e] contains the nth permutation
    return perm[:e]

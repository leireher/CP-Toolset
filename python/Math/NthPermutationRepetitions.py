from math import factorial
from collections import defaultdict

def nthPermutationRepetitions(inp, n):
    mp = defaultdict(int)
    for i in range(len(inp)):
        mp[inp[i]] += 1

    buffer = ["" for _ in range(len(inp))]
    total = 0
    for i in range(len(inp)):
        for key in mp.keys():
            if mp[key] > 0:
                mp[key] -= 1
                perm = factorial(len(inp) - i - 1)
                
                for value in mp.values():
                    perm = perm // factorial(value)
                
                if n < total + perm:
                    buffer[i] = key
                    break

                total += perm
                mp[key] += 1

    return "".join(buffer)

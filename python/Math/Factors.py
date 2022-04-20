# O(sqrt(n))
# Returns a list of all the factors of n
# Example: n = 12 -> result = [2, 2, 3]
# n > 1
def factors(n):
    z = 2
    results = []
    while(z*z<=n):
        if(n%z==0):
            results.append(int(z))
            n /= z
        else:
            z += 1
    if(n>1):
        results.append(int(n))
    return results

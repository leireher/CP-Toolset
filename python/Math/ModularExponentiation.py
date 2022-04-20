# Complexity: O(log b)
# Returns (a**b)%c
def modular_pow(a, b, c):
    ans = 1
    while b > 0:
        if b % 2 == 1:
            ans = (ans * a) % c
        b = b >> 1
        a = (a * a) % c
    return ans

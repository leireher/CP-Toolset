# This is a collection of useful code for solving problems that
# involve modular linear equations.  Note that all of the
# algorithms described here work on nonnegative integers.

# return a % b (positive value)
def mod(a, b):
    return ((a % b) + b) % b

# computes gcd(a, b)
def gcd(a, b):
    while b != 0:
        a %= b
        a, b = b, a
    return a

# computes lcm(a,b)
def lcm(a, b):
    return a // gcd(a, b) * b

# returns (d, x, y) where d = gcd(a,b) && d = ax + by
def extended_euclid(a, b):
    xx = y = 0
    yy = x = 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - q * xx
        y, yy = yy, y - q * yy

    return a, x, y

# finds all solutions to ax = b (mod n)
def modular_linear_equation_solver(a, b, n):
    solutions = []
    d, x, y = extended_euclid(a, n)
    if b % d == 0:
        x = mod(x * (b // d), n)
        for i in range(d):
            solutions.append(mod(x + i * (n // d), n))
            
    return solutions

# computes b such that ab = 1 (mod n), returns -1 on failure
def mod_inverse(a, n):
    d, x, y = extended_euclid(a, n)
    return -1 if d > 1 else mod(x, n)

# Chinese remainder theorem (special case): find z such that
# z % x = a, z % y = b.  Here, z is unique modulo M = lcm(x,y).
# Return (z,M).  On failure, M = -1.
def chinese_remainder_theorem(x, a, y, b):
    d, s, t = extended_euclid(x, y)
    if a % d != b % d:
        return 0, -1

    return (
        mod(s * b * x + t * a * y, x * y) // d,
        x * y // d
    )

# Chinese remainder theorem: find z such that
# z % x[i] = a[i] for all i.  Note that the solution is
# unique modulo M = lcm_i (x[i]).  Return (z,M).  On 
# failure, M = -1.  Note that we do not require the a[i]'s
# to be relatively prime.
def chinese_remainder_theorem_system(x, a):
    ans = a[0], x[0]
    for i in range(1, len(x)):
        ans = chinese_remainder_theorem(ans[1], ans[0], x[i], a[i])
        if ans[1] == -1:
            break
    return ans

# computes x and y such that ax + by = c; on failure, x = y = -1
def linear_diophantine(a, b, c):
    d = gcd(a, b)
    if c % d != 0:
        return -1, -1
    else:
        x = c // d * mod_inverse(a // d, b // d)
        y = (c - a * x) // b
        return x, y

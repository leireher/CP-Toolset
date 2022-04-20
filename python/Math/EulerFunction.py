# Euler's Totient Function
# Amount of numbers 1..n that are relatively prime to n
# a^phi(N) = 1 (mod N) if gcd(a, N) = 1
# O(n^(1/2) log n)
def phi(n): 
    # Initialize result as n
    result = n
    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    p = 2
    while(p * p <= n):
         
        # Check if p is a
        # prime factor.
        if (n % p == 0):
            # If yes, then
            # update n and result
            while (n % p == 0):
                n = int(n / p);
            result -= int(result / p)
        p += 1;
 
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most
    # one such prime factor)
    if (n > 1):
        result -= int(result / n)
    return result

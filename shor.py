import random

# Takes N > 1 and finds a nontrivial factor of N, if it exists.
def shor(N, tries=1000):
    for i in range(tries):
        ##################################################################
        # 1. Find random a < N such that a and N are coprime
        # (if a and N are not coprime, it means we already found a factor)
        ##################################################################
        a = random.randint(2, N - 1)
        factor = gcd(N, a)
        # The easy case
        if factor != 1: return factor

        #################################################
        # 2. Use the period-finding subroutine to find r, 
        # the order of a in Z*_N
        #################################################
        r = findPeriod(N, a)
        
        ########################################################
        # 3. If r is even and a ** (r/2) mod N != N-1 we're done
        # Otherwise repeat
        ########################################################
        if r % 2 == 0:
            if modPower(a, r/2, N) != N-1:
                factor = gcd(a ** (r/2) - 1, N)
                return factor

    print("Failed to find factor!")
    return None

# Calculates the greatest common divisor of a and b
# Using euclid's algorithm
def gcd(a, b):
    if a < b:
        # Parallel assignment just because we can!
        a, b = b, a
    # Now a is the larger one
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Calculates x^m mod N
def modPower(x, m, N):
    if m == 0:
        return 1
    else:
        if m % 2 == 0:
            return (modPower(x, m / 2, N) ** 2) % N
        else:
            return (modPower(x, m / 2, N) ** 2 * x) % N

# Finds the period of the function f(x) = a ** x % N
# In other words, the order r of a in Z*_N
# Or in other words, the smallest r > 0 such that a ** r % N == 1
def findPeriod(N, a):
    # Replace this classical algorithm with a quantum one!
    temp = 1
    for r in range(1, N):
        temp = (temp * a) % N
        if temp == 1:
            return r
    # It is impossible to reach here
    return None

if __name__ == '__main__':
    print(shor(373 * 379))

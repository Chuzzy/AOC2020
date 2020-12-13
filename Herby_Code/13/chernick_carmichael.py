from math import sqrt, prod
from sympy import prime, primepi, primerange


def factor(n):
      factors = set()
      for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
          factors.add(x)
          factors.add(n//x)
      return factors


def is_prime(n):
    return len(factor(n)) == 2

def U(n, m):
    return (6*m + 1) * (12 * m + 1) * prod(2**i * 9 * m + 1 for i in range(1, n-1)) 

def U_carmichael(n, m):
    U_ = U(n, m)
    return (n <= 4 or m % 2**(n-4) == 0) and all( U_ % p**2 != 0 for p in primerange(1, U_) if U_ % p == 0)

print(U_carmichael(3, 1))
print(U_carmichael(4, 1))
print(U_carmichael(5, 7))
print(U_carmichael(5, 380))
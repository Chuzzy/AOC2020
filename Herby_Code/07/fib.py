cache = {}
def fib(n):
    if n <= 2:
        return 1

    if (LHS := cache.get(n-1)) == None:
        LHS = cache[n-1] = fib(n-1)

    if (RHS := cache.get(n-2)) == None:
        RHS = cache[n-2] = fib(n-2)

    return LHS + RHS

def fib_naive(n):
    if n <= 2:
        return 1
    return fib_naive(n-1) + fib_naive(n-2)

from time import time

naive = time()
print(fib_naive(40))
print('Naive time:', time() - naive)
faster = time()
print(fib(40))
print('Faster time:', time() - faster)
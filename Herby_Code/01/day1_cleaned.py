inp = {int(l) for l in open('input1.txt', 'r').readlines()}

"""
def sum2(n):
    for i in inp:
        if n-i in inp:
            return i * (n-i)


print(sum2(2020))

for j in inp:
    if sum2(2020-j):
        print(j * sum2(2020-j))
        break
"""

from itertools import combinations
from math import prod

def sum_n(xs, n):
    return {sum(Y): prod(Y) for Y in combinations(xs, n)}[2020]

print(sum_n(inp, 2))
print(sum_n(inp, 3))

"""
part1 = True

for i in inp:
    if part1 and 2020 - i in inp:
        print(i * (2020-i))
        part1 = False
    
    for j in inp:
        if 2020 - i - j in inp:
            print(i * j * (2020 - i - j))
            break
"""
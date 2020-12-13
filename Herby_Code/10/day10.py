from math import prod
from itertools import chain, combinations



adaptors = [int(x) for x in """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".splitlines()]

adaptors = [int(x) for x in open('input10.txt').readlines()]


built_in = 3 + max(adaptors)

#adaptors.append(built_in)
#adaptors.append(0)
adaptors += [built_in, 0]
adaptors.sort()

diff = lambda ys: [*map(lambda xs: xs[0]-xs[1], zip(ys[1:], ys))]

#diffs = [*map(lambda xs: xs[0]-xs[1], zip(adaptors[1:], adaptors))]
diffs = diff(adaptors)

#print(diffs)

def split_n(xs, n):
    group = []    
    for num in xs:
        if num != n:
            group.append(num)
        elif group:
            yield group
            group = []

def combos(xs):
    return chain(combinations(xs, n) for n in range(1, len(xs) + 1))

def count(xs):
    pass

print('Part 1:', diffs.count(1) * diffs.count(3))
#print('Part 2:', prod(count(x) for x in diffs.split(3)))

#xs = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
#print(diff(adaptors))
#print(list(list(x) for x in combos(adaptors)))

from collections import defaultdict

adaptors = adaptors[1:-1]

dp = defaultdict(int)
dp[0] = 1
for x in adaptors:
    dp[x] += dp[x-1] + dp[x-2] + dp[x-3]


print(len(adaptors))
print(adaptors)
print(dp[adaptors[-1]])


total = 0
print('\n\n\n')
for i in range(1, len(adaptors)):
    for combo in combinations(adaptors, i):
        if len(combo) >= 2:
            #print(combo)
            #print(diff(combo))
            if max(diff(combo)) <= 3:
                total += 1

print(total)
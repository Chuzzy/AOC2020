from time import time
from itertools import product
#from collections import defaultdict

def neighbours(coord, dim = 3):
    for delta in product([0, 1, -1], repeat = dim):
        yield tuple(x + y for x, y in zip(coord, delta))

def active_neighbours(coord, space, dim = 3):
    return sum(nb in space for nb in neighbours(coord, dim)) - (coord in space)

def update(space, dim) -> frozenset():
    to_be_updated = set()
    updates = set()

    for coord in space:
        to_be_updated.update(set(neighbours(coord, dim)))

    for coord in to_be_updated:
    #for coord in set().union(set(neighbours(coord, dim)) for coord in space):
        t = active_neighbours(coord, space, dim)
        if (coord in space and (t == 2 or t == 3)) or (coord not in space and t == 3):
            updates.add(coord)

    return frozenset(updates)
    #return set(updates)

initial = """.#.
..#
###""".splitlines()

initial = open('input17.txt', 'r').read().splitlines()

now = time()

"""
space3 = set()
space4 = set()

for y in range(len(initial)):
    for x in range(len(initial[0])):
        if initial[y][x] == '#':
            space3.add((x, y, 0))
            space4.add((x, y, 0, 0))

space3, space4 = frozenset(space3), frozenset(space4)
"""
ylen, xlen = len(initial), len(initial[0])

initial_coords = [(x, y) for x in range(xlen) for y in range(ylen) if initial[y][x] == '#']

space3 = frozenset((*coord, 0) for coord in initial_coords)
space4 = frozenset((*coord, 0, 0) for coord in initial_coords)

for t in range(6):
    space3 = update(space3, 3)
    space4 = update(space4, 4)

print('Silver:', len(space3), '\nGold:', len(space4))

print(time() - now)
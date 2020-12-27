from collections import defaultdict
from functools import reduce

from time import time
now = time()

add = lambda xs, ys: tuple(x + y for x, y in zip(xs, ys))

"""
dirs = {
    'e': (1, -1, 0),
    'w': (-1, 1, 0),
    'ne': (1, 0, -1),
    'nw': (0, 1, -1),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1)
    }
"""

# Consider hex points as points in plane defined by x + y + z = 0 in Z^3
# -> can ignore third coord (y = - (x + y))

dirs = {
    'e': (1, -1),
    'w': (-1, 1),
    'ne': (1, 0),
    'nw': (0, 1),
    'se': (0, -1),
    'sw': (-1, 0)
    }

dirs_vals = set(dirs.values())
dirs_keys = set(dirs.keys())

def parse(text):
    while len(text) > 0:
        if text[:1] in dirs_keys:
            yield text[:1]
            text = text[1:]
        elif text[:2] in dirs_keys:
            yield text[:2]
            text = text[2:]

# Contains black tiles
tiles = set()

inp = open('input24.txt').read().splitlines()

for line in inp:
    seq = [dirs[x] for x in parse(line)]

    point = reduce(add, seq)

    if point in tiles:
        tiles.remove(point)
    else:
        tiles.add(point)

print('Silver:', len(tiles))

print(time() - now)
now = time()

adjacent = lambda tile: [add(tile, d) for d in dirs_vals]

def adjacent_count(coord, tiles):
    return sum(adj in tiles for adj in adjacent(coord))

def update(tiles):
    updates = set()
    
    for coord in set(tiles).union(*[adjacent(tile) for tile in tiles]):
        adj = adjacent_count(coord, tiles)
        
        if (coord in tiles and 1 <= adj <= 2) or (coord not in tiles and adj == 2):
            updates.add(coord)

    return updates

for _ in range(100):
    tiles = update(tiles)

print('Gold:', len(tiles))

print(time() - now)
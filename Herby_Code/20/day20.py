from math import prod
from collections import defaultdict
from itertools import permutations, product

def show(tile):
    print(*list(t for t in tile), sep = '\n', end = '\n\n')

def edge(tile, r):
    """Clockwise order, r = 0 <-> top etc"""
    if r == 0:
        edge = tile[0]
    elif r == 1:
        edge = ''.join([t[-1] for t in tile])
    elif r == 2:
        edge = tile[-1][::-1]
    elif r == 3:
        edge = ''.join([t[0] for t in tile[::-1]])

    return edge

def rotate(r, tile):
    if r == 0:
        return tile
    elif r == 1:
        return [''.join(x[::-1]) for x in zip(*tile)]
    elif r == 2:
        return [t[::-1] for t in tile[::-1]]
    elif r == 3:
        return [''.join(x) for x in zip(*tile)][::-1]


def flip(tile):
    """Flip top -> bottom"""
    return tile[::-1]

def match_border(tile1, tile2):
    for i in range(4):
        e1 = edge(tile1, i)

        for j in range(4):
            #e2 = edge(tile2, j)
            if e1 == edge(tile2, j):
                return (i, j, False)
            elif e1 == edge(flip(tile2), j):
                return (i, j, True)
    
    return None

def match_edge_tile(e, tile):
    for r in range(4):
        if e == edge(tile, r): return r
    
    return None

def dir(xy, r):
    if r == 0:
        return (xy[0], xy[1] + 1)
    elif r == 1:
        return (xy[0] + 1, xy[1])
    elif r == 2:
        return (xy[0], xy[1] - 1)
    elif r == 3:
        return (xy[0] - 1, xy[1])

###############
# Part 1 code #
###############

with open('example.txt', 'r') as file:
    inp = file.read().strip('\n').split('\n\n')

tiles = {int(l[0][5:9]): l[1:] for l in map(str.splitlines, inp)}
matches = {}

for id1, tile in tiles.items():
    for id2, tile2 in tiles.items():
        if id1 != id2 and (m := match_border(tile, tile2)) != None:
            mi, ma = min(id1, id2), max(id1, id2)
            matches[(mi, ma)] = m

num_matches = defaultdict(int)

for id1, id2 in matches.keys():
    num_matches[id1] += 1
    num_matches[id2] += 1

#print(num_matches)

corners = [id_ for id_ in tiles.keys() if num_matches[id_] == 2]

print(*corners)
print('Silver:', prod(corners))

###############
# Part 2 code #
###############

combos = [(0, (0, 1)), (1, (1, 0)), (2, (0, -1)), (3, (-1, 0))]
switch = {0:1, 1:3, 2:0, 3:1}


def fits_exactly(grid, coord, tile):
    for r, dxy in combos:
        xy = (coord[0] + dxy[0], coord[1] + dxy[1])
        if xy in grid.keys():
            if edge(tile, r) != edge(grid[xy], switch[r]):
                return False
    
    return True

def fits(grid, coord, tile):
    for r in range(4):
        if fits_exactly(grid, coord, rotate(r, tile)):
            return rotate(r, tile)
        elif fits_exactly(grid, coord, rotate(r, flip(tile))):
            return rotate(r, flip(tile))
    
    return None

edges = {}

for id1, tile1 in tiles.items():
    for id2, tile2 in tiles.items():
        if id1 == id2: continue
        for i in range(4):
            for j in range(4):
                mi, ma = min(id1, id2), max(id1, id2)
                if edge(tile1, i) == edge(tile2, j):
                    edges[(mi, ma)] = (i, j, False)
                if edge(tile1, i) == edge(flip(tile2), j):
                    edges[(mi, ma)] = (i, j, True)

"""
for k, v in edges.items():
    print(f'{k} - {v}')
"""

grid = {(0, 0): (corners[0], False)}

added = set(tiles.keys())
added.remove(corners[0])

while len(added) > 0:
    update = None
    #found = False
    for coord, t in grid.items():
        id1, flipped1 = t
        for _, dxy in combos:
            xy = (coord[0] + dxy[0], coord[1] + dxy[1])
            if (0 <= xy[0] <= 2) and (0 <= xy[1] <= 2) and (xy not in grid.keys()):
                for id2 in added:
                    #print(id1, id2)
                    mi, ma = min(id1, id2), max(id1, id2)

                    if (mi, ma) in edges.keys():
                        
                        i2, j2, flipped2 = edges[(mi, ma)]

                        r = 0

                        update = (xy, (id2, flipped1 != flipped2))
                        added.remove(id2)
                        break
            if update != None: break
        if update != None: break
    
    grid[update[0]] = update[1]

print(grid)
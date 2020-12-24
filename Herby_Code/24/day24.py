from collections import defaultdict
from functools import reduce

inp = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".splitlines()

from time import time
now = time()

inp = open('input24.txt', 'r').read().splitlines()

add = lambda xs, ys: tuple(x + y for x, y in zip(xs, ys))
ZERO = (0, 0, 0)

tile_dirs = [
    (1, -1, 0),
    (1, 0, -1),
    (0, 1, -1),
    (-1, 1, 0),
    (-1, 0, 1),
    (0, -1, 1)
]


# Cube coordinates
#tiles = [[], [], []]

dirs = ['e', 'se', 'sw', 'w', 'nw', 'ne']

dirs_map = {'e': (1, -1, 0), 'w': (-1, 1, 0), 'ne': (1, 0, -1), 'nw': (0, 1, -1), 'se': (0, -1, 1), 'sw': (-1, 0, 1)}

def parse(text):
    while len(text) > 0:
        if text[:1] in dirs:
            yield text[:1]
            text = text[1:]
        elif text[:2] in dirs:
            yield text[:2]
            text = text[2:]
        else:
            print('??????', text)

flipped = defaultdict(bool)

#print(inp[0])
#test = list(parse(inp[0]))
#print(test)
#test2 = [dirs_map[x] for x in test]
#print(reduce(add, test2))

for l in inp:
    seq = [dirs_map[x] for x in parse(l)]
    
    pt = reduce(add, seq)

    if flipped[pt]:
        del(flipped[pt])
    else:
        flipped[pt] = True
    #flipped[pt] = not flipped[pt]

#print(sum(flipped.values()))
print('Part 1:', len(flipped))

adjacent = lambda tile: [add(tile, d) for d in tile_dirs]

def adjacent_count(coord, tiles):
    return sum(tiles[adj] for adj in adjacent(coord))

def update(tiles):
    updates = defaultdict(bool)
    
    for coord in set(tiles.keys()).union(*[adjacent(tile) for tile in tiles.keys()]):
        adj = adjacent_count(coord, tiles)
        if tiles[coord] and (adj == 0 or adj > 2): # Black
            pass
            #del(flipped[coord])
        elif tiles[coord] and (adj == 1 or adj == 2):
            updates[coord] = True
        elif not tiles[coord] and adj == 2:
            updates[coord] = True

    return updates

for i in range(100):
    #print(i, len(flipped))
    flipped = update(flipped)

print(len(flipped))

print(time() - now)
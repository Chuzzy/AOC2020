from itertools import product
from collections import defaultdict

def neighbours(coord, dim = 3):
    for delta in product([0, 1, -1], repeat = dim):
        yield tuple(x+y for x, y in zip(coord, delta))

def active_neighbours(coord, space, dim = 3):
    #total = 0
    #for neighbour in neighbours(coord, dim):
    #    total += space[neighbour]
    
    #return total - space[coord]
    return sum(space[nb] for nb in neighbours(coord, dim)) - space[coord]

def update(space, dim):
    to_be_updated = set()
    updates = defaultdict(int)

    for coord in space.keys():
        to_be_updated.update(set(neighbours(coord, dim)))

    for coord in to_be_updated:
        t = active_neighbours(coord, space, dim)
        if (space[coord] == 1 and (t == 2 or t == 3)) or (space[coord] == 0 and t == 3):
            updates[coord] = 1

    return updates

initial = """.#.
..#
###""".splitlines()

#initial = open('input17.txt', 'r').read().splitlines()

space = defaultdict(int)
space2 = defaultdict(int)

for y in range(len(initial)):
    for x in range(len(initial[0])):
        if initial[y][x] == '#':
            space[(x, y, 0)] = 1
            space2[(x, y, 0, 0)] = 1

for t in range(6):
    space = update(space, 3)
    space2 = update(space2, 4)

print('Silver:', sum(space.values()))
print('Gold:', sum(space2.values()))
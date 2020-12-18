from itertools import product
from collections import defaultdict

def neighbours(x, y, z, space):
    for dx, dy, dz in product([0, 1, -1], repeat = 3):
        yield (x + dx, y + dy, z + dz)

def active_neighbours(x, y, z, space):
    total = 0
    for neighbour in neighbours(x, y, z, space):
        total += space[neighbour]
    
    return total - space[(x, y, z)]

def update(space):
    to_be_updated = set()
    updates = dict()

    for coord in space.keys():
        to_be_updated.update(set(neighbours(*coord, space)))

    for coord in to_be_updated:
        t = active_neighbours(*coord, space)
        if space[coord] == 1 and (t != 2 and t != 3):
            updates[coord] = 0
        if space[coord] == 0 and t == 3:
            updates[coord] = 1
    
    for k, v in updates.items():
        space[k] = v

def neighbours2(x, y, z, w, space):
    for dx, dy, dz, dw in product([0, 1, -1], repeat = 4):
        yield (x + dx, y + dy, z + dz, w + dw)

def active_neighbours2(x, y, z, w, space):
    total = 0
    for neighbour in neighbours2(x, y, z, w, space):
        total += space[neighbour]
    
    return total - space[(x, y, z, w)]

def update2(space):
    to_be_updated = set()
    updates = dict()

    for coord in space.keys():
        to_be_updated.update(set(neighbours2(*coord, space)))

    for coord in to_be_updated:
        t = active_neighbours2(*coord, space)
        if space[coord] == 1 and (t != 2 and t != 3):
            updates[coord] = 0
        if space[coord] == 0 and t == 3:
            updates[coord] = 1
    
    for k, v in updates.items():
        space[k] = v

def show_space(xmax, ymax, zmax, space):
    for z in range(-zmax, zmax + 1):
        print('z =', z)
        
        for y in range(-ymax, ymax + 1):
            for x in range(-xmax, xmax + 1):
                print(['.', '#'][space[(x, y, z)]], end = '')
            print()
        
        print()

space = defaultdict(int)
space2 = defaultdict(int)

initial = """.#.
..#
###""".splitlines()

initial = open('input17.txt', 'r').read().splitlines()


for y in range(len(initial)):
    for x in range(len(initial[0])):
        #print(int(initial[y][x] == '#'), 'coord', end = ' ')
        #print(x, y)
        space[(x, y, 0)] = int(initial[y][x] == '#')
        space2[(x, y, 0, 0)] = int(initial[y][x] == '#')

for t in range(6):
    #print('Time:', t)
    #show_space(6, 6, 2, space)
    #print('\n\n')

    update(space)
    update2(space2)

print('Silver:', sum(space.values()))
print('Gold:', sum(space2.values()))
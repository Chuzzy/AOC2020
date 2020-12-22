from math import sqrt, prod
from collections import defaultdict
from itertools import product, permutations

class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y
    def from_tuple(self, xy):
        self.x, self.y = xy
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f'Point({self.x}, {self.y})'
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

def connect(A, B):
    # A -> B
    if right(A) == left(B):
        return (1, 0)
    elif left(A) == right(B):
        return (-1, 0)
    elif top(A) == bottom(B):
        return (0, 1)
    elif bottom(A) == top(B):
        return (0, -1)

def show(tile):
    print(*list(t for t in tile), sep = '\n', end = '\n\n')

def show_grid(grid, N):
    n = len(grid[Point(0, 0)])
    for y in range(N):
        for y2 in range(n):
            for x in range(N):
                for x2 in range(n):
                    s = grid.get(Point(x, y))
                    if s == None:
                        print(' ', end = '')
                    else:
                        print(s[y2][x2], end = '')
                print(' ', end = '')
            print()
        print()


rotateL = lambda tile: [''.join(t) for t in zip(*tile)][::-1]
rotateR = lambda tile: [''.join(t[::-1]) for t in zip(*tile)]
flipY = lambda tile: tile[::-1]
middle = lambda ts: [t[1:-1] for t in ts[1:-1]]

#top = lambda tile: tile[0]
#bottom = lambda tile: tile[-1][::-1]
#left = lambda tile: ''.join(t[0] for t in tile)[::-1]
#right = lambda tile: ''.join(t[-1] for t in tile)

top = lambda tile: tile[0]
bottom = lambda tile: tile[-1]
left = lambda tile: ''.join(t[0] for t in tile)
right = lambda tile: ''.join(t[-1] for t in tile)

sides = lambda tile: [top(tile), right(tile), bottom(tile), left(tile)]
sides2 = lambda tile: sides(tile) + sides(flipY(tile))

#directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
directs = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]
#around = lambda xs: set((xs[0]+d[0], xs[1]+d[1]) for d in directs)
around = lambda xs: set(xs + d for d in directs)
#around2 = lambda xs, N: [xy for xy in around(xs) if 0<=xy[0]<N and 0<=xy[1]<N]
around2 = lambda xs, n: [xy for xy in around(xs) if 0 <= xy.x < n and 0 <= xy.y < n]

basics = lambda t: [t, rotateL(t), rotateL(rotateL(t)), rotateR(t), flipY(t), rotateL(flipY(t)), rotateL(rotateL(flipY(t))), rotateR(flipY(t)), ]

with open('input20.txt', 'r') as file:
    inp = file.read().strip('\n').split('\n\n')

tiles = {int(l[0][5:9]): l[1:] for l in map(str.splitlines, inp)}
N = int(sqrt(len(tiles)))

tiles2 = {k: basics(v) for k, v in tiles.items()}

adjacent = defaultdict(set)
adj2 = set()
for id in tiles.keys():
    for id2 in tiles.keys():
        if id != id2 and set(sides2(tiles[id])) & set(sides2(tiles[id2])) != set():
                adj2.add((id, id2))
                adjacent[id].add(id2)

#grid = [[0] * N for _ in range(N)]
corners = [k for k, v in adjacent.items() if len(v) == 2]


print([id for id in tiles.keys() if len(adjacent[id]) == 2])
# Classic, this is too big, use the other sol I guess
print('Silver', prod(corners))

"""
show(tiles[1951])
for x in sides(tiles[1951]):
    print(x)

input()
"""

# basics(corners[1])[0] works
t = 0

grid = {Point(0, 0): basics(tiles[corners[1]])[t]}
grid2 = {Point(0, 0): corners[1]}
#print(grid2)
added = set(tiles.keys())
added.remove(grid2[Point(0, 0)])

#print(added)

def fits(grid, coord, tile, N):
    if (s := grid.get(coord + Point(0, 1))) != None and bottom(tile) != top(s):
        return False
    elif (s := grid.get(coord + Point(1, 0))) != None and right(tile) != left(s):
        return False
    elif (s := grid.get(coord + Point(0, -1))) != None and top(tile) != bottom(s):
        return False
    elif (s := grid.get(coord + Point(-1, 0))) != None and left(tile) != right(s):
        return False

    return True

while len(added) > 0:
    for xy in set(xy for coord in grid.keys() for xy in around2(coord, N) if xy not in grid.keys()):
        #print(xy)
        new = False

        for id in added:
            for tile in basics(tiles[id]):
                if fits(grid, xy, tile, N):
                    
                    #for xy2 in around2(xy, N):
                    #    if xy2 in grid2.keys():
                            #print((id, grid2[xy2]) in adj2)

                    new_tile = tile
                    new_point = xy
                    new_id = id
                    new = True
                    break
                if new: break
            if new: break
        if new: break
    
    if not new:
        for t in basics(tiles[1427]):
            print(fits(grid, Point(1, 1), t, N))
        print('???????')
        input()
    #print(f'\nAdding {new_id} at {new_point}')
    grid[new_point] = new_tile
    grid2[new_point] = new_id
    added.remove(new_id)

    #print(grid2)
    #show_grid(grid, N)

    #input()

#show_grid(grid, N)

grid3 = {k: middle(v) for k, v in grid.items()}

#show_grid(grid3, N)
n2 = len(grid3[Point(0, 0)])
#print('n2', n2)


pic = [['' for _ in range(n2 * N)] for _ in range(n2 * N)]

for y in range(N):
    for y2 in range(n2):
        for x in range(N):
            for x2 in range(n2):
                s = grid3.get(Point(x, y))
                if s == None:
                    print('??????????')
                else:
                    #print(s[y2][x2], end = '')

                    pic[n2 * y + y2][n2 * x + x2] = s[y2][x2]
        #print()

# Printing out the picture
#for y in range(len(pic)):
#    print(*[x for x in pic[y]], sep = '', end = '\n')

monster = (
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
        )

print(len(monster), len(monster[0]))
monster = set(Point(x, y) for x in range(len(monster[1])) for y in range(len(monster)) if monster[y][x] == '#')

match_point = lambda pt, pict: pict[pt.y][pt.x] == '#'


monsterpts = set()
pic = rotateR(pic)

monster_count = 0

for y in range(len(pic) - 3):
    for x in range(len(pic) - 20):
        if all(match_point(pt + Point(x, y), pic) for pt in monster):
            for pt in monster:
                monsterpts.add(pt + Point(x, y))
            monster_count += 1

print(monster_count)

hashes = sum(l.count('#') for l in pic)
print('Gold:', hashes - len(monsterpts))
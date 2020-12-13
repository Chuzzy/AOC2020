from copy import deepcopy

adjacents = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]

grid = [list(x) for x in """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()]

grid = [list(x) for x in open('input11.txt').readlines()]

#print(grid)

inbounds = lambda x, y, xmax, ymax: 0 <= x < xmax and 0 <= y < ymax

def count_adjacent(grid, x, y):
    total = 0
    for dx, dy in adjacents:
        if inbounds(x+dx, y+dy, len(grid[0]), len(grid)):
            total += grid[y+dy][x+dx] == '#'
    
    return total


def update(grid):
    newgrid = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c_adj = count_adjacent(grid, x, y)

            if grid[y][x] == 'L' and c_adj == 0:
                newgrid[y][x] = '#'
            elif grid[y][x] == '#' and c_adj >= 4:
                newgrid[y][x] = 'L'
    
    return newgrid

def find_direc(grid, x, y, dx, dy):
    i = 1
    while inbounds(x + i*dx, y + i*dy, len(grid[0]), len(grid)):
        if grid[y + i*dy][x+ i*dx] != '.':
            return grid[y + i*dy][x + i*dx]
        i += 1
    
    return '.'

def see_count(grid, x, y):
    total = 0
    for dx, dy in adjacents:
        total += find_direc(grid, x, y, dx, dy) == '#'

    return total

def update2(grid):
    newgrid = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c_adj = see_count(grid, x, y)

            if grid[y][x] == 'L' and c_adj == 0:
                newgrid[y][x] = '#'
            elif grid[y][x] == '#' and c_adj >= 5:
                newgrid[y][x] = 'L'
    
    return newgrid

orig = deepcopy(grid)

last = []
i = 0
while grid != last:
    i += 1
    #print(grid)
    last = deepcopy(grid)
    grid = update(grid) 

print(i)
print(sum(r.count('#') for r in grid))

last = []
grid = orig
i = 0
while grid != last:
    i += 1
    #print(grid)
    last = deepcopy(grid)
    grid = update2(grid)

print(sum(r.count('#') for r in grid))

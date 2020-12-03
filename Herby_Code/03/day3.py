from math import prod

inp = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split()

inp = open('input3.txt', 'r').read().split()

def part1(inp, dx, dy):
    x, y, trees = dx, dy, 0

    while y < len(inp):
        trees += inp[y][x % len(inp[0])] == '#'
        x += dx
        y += dy
    
    return trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print('Silver:', part1(inp, 3, 1))
print('Gold:', prod(part1(inp, *xs) for xs in slopes))
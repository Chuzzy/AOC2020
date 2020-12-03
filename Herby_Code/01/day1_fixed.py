inp = [int(x) for x in open('input1.txt', 'r').readlines()]

"""def part1(inp, n):
    for i, x in enumerate(inp):
        if n - x in inp[i+1:]:
            return x * (n-x)"""

def part1(inp, n):
    comp = set()
    for i in inp:
        if i in comp:
            return i * (n-i)
        
        comp.add(n-i)

def part2(inp, n):
    for j in inp:
        if x := part1(inp, n-j):
            return x * j

print('Silver:', part1(inp, 2020))
print('Gold:', part2(inp, 2020))
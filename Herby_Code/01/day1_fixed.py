inp = [int(x) for x in open('input1.txt', 'r').readlines()]

def part1(inp, n):
    for i, x in enumerate(inp):
        if n - x in inp[i+1:]:
            return x * (n-x)


print(part1(inp, 2020))
print(part1([1, 1], 2020))
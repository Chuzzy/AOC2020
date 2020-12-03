inp = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split('\n')

inp = [x for x in open('input2.txt', 'r').readlines()]


def valid1(t):
    a, b, c = t.split(' ')
    u, v = list(map(int, a.split('-')))

    return u <= c.count(b[0]) <= v

def valid2(t):
    a, b, c = t.split(' ')
    u, v = list(map(int, a.split('-')))

    return (c[u-1] == b[0]) != (c[v-1] == b[0])

print("Part 1:", sum(map(valid1, inp)))
print("Part 2:", sum(map(valid2, inp)))
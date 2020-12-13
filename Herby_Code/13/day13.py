inp = """939
7,13,x,x,59,x,31,19""".splitlines()

inp = open('input13.txt').readlines()
time, buses = inp

time = int(time)
buses = [int(x) for x in buses.split(',') if x != 'x']

result = min([(-time % bus, bus) for bus in buses], key = lambda x: x[0])
print('Silver:', result[0] * result[1])

_, buses = inp

buses = [(int(x), i) for i, x in enumerate(buses.split(',')) if x != 'x']
print(buses)

from math import prod, gcd
prod_ = prod(bus[0] for bus in buses)
print(prod_)

ys = {}

def totient(n):
    return sum(gcd(n, i) == 1 for i in range(1, n))

for busn, _ in buses:
    ys[busn] = (prod_ // busn) ** totient(busn) % prod_

part2 = lambda t: all((t + i) % x == 0 for x, i in buses)

sol = sum(ys[busn] * -i for busn, i in buses)

print(sol % prod_)
print(part2(sol % prod_))
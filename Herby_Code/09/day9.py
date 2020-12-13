inp = [int(x) for x in """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()]

with open('input9.txt', 'r') as file:
    inp = [int(l) for l in file.readlines()]

# Modified from day 1
# (Doesn't accept repeats e.g. [2], 4)
def sums(xs, n):
    comp = set() # Complement set
    for i in xs:
        if i in comp:
            return True
        
        comp.add(n-i)
    
    return False

def part1(xs, shift):
    for i, n in enumerate(xs[shift + 1:]):
        if not sums(xs[i + 1:i + shift + 1], n):
            return n

def part2(xs, s):
    for i in range(len(xs)):
        for j in range(len(xs) - i + 1):
            if sum(xs[i:j]) == s:
                return min(xs[i:j]) + max(xs[i:j])

print('Silver:', s := part1(inp, 25))
print('Gold:', part2(inp, s))
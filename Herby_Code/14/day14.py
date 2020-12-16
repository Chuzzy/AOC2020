from copy import copy
from itertools import product

bit_mask = lambda xy: xy[1] if xy[0] == 'X' else int(xy[0])

#def bit_mask(x, y):
#    if xy[0] == 'X

bin_to_dec = lambda xs: sum(2**i * x for i, x in enumerate(xs[::-1]))

def dec_to_bin(y):
    pass

def apply_mask(xs, y):
    # x mask, y int
    ys = []
    while y > 0:
        ys.append(y % 2)
        y //= 2
    
    ys = [0] * (len(xs) - len(ys)) + ys[::-1]
    #return zip(xs, ys)
    return bin_to_dec([*map(bit_mask, zip(xs, ys))])

def adr_bit_mask(x, y):
    if x == '0':
        return y
    elif x == '1':
        return 1
    else:
        return 'X'

def replace(full, replacements):
    indices = [i for i, x in enumerate(full) if x == 'X']
    #print('ind', indices)
    for rep in replacements:
        #print('rep', rep)
        for i, r in zip(indices, rep):
            full[i] = r
        #print('full', full)
        yield copy(full)

def adr_mask(xs, y):
    ys = []
    while y > 0:
        ys.append(y % 2)
        y //= 2
    
    ys = [0] * (len(xs) - len(ys)) + ys[::-1]
    adrs = []
    adr = [*map(lambda xs: adr_bit_mask(*xs), zip(xs, ys))]
    N = adr.count('X')

    return list(replace(adr, product([0, 1], repeat = N)))


inp = open('input14.txt', 'r').read().splitlines()

if False:
    inp = """mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1""".splitlines()

mem = {}
mem2 = {}
mask = ""

for line in inp:
    opcode, _, operand = line.split(' ')
    if opcode == 'mask':
        mask = operand
    else:
        #print('operand', int(operand))
        for adr in adr_mask(mask, int(opcode[4:-1])):
            #print(bin_to_dec(adr))
            mem2[bin_to_dec(adr)] = int(operand)
        mem[int(opcode[4:-1])] = apply_mask(mask, int(operand))

print(sum(mem.values()))
print(sum(mem2.values()))

#print(["".join(map(str, x)) for x in adr_mask("000000000000000000000000000000X1001X", 42)])



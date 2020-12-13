actions = """F10
N3
F7
R90
F11""".splitlines()

with open('input12.txt', 'r') as file:
    actions = file.read().splitlines()

directions = ['N', 'E', 'S', 'W']

n_factor = {'N': 1, 'E': 0, 'S': -1, 'W': 0}
e_factor = {'N': 0, 'E': 1, 'S': 0, 'W': -1}

n, e = 0, 0
wn, we, n2, e2 = 1, 10, 0, 0
direction, direction_i = 'E', 1

for action in actions:
    d = action[0]
    a = int(action[1:])

    if d == 'F':
        d = direction
        n += n_factor[d] * a
        e += e_factor[d] * a

        n2 += wn * a
        e2 += we * a

    elif d in directions:
        n += n_factor[d] * a
        e += e_factor[d] * a

        wn += n_factor[d] * a
        we += e_factor[d] * a
    elif d == 'L':
        direction_i -= a // 90
        direction_i %= 4
        direction = directions[direction_i]

        for _ in range(a//90):
            wn, we = we, -wn

    elif d == 'R':
        direction_i += a // 90
        direction_i %= 4
        direction = directions[direction_i]

        for _ in range(a//90):
            wn, we = -we, wn

    #print(e2, n2, direction)
    #print(we, wn)

#print(n, e)
print(abs(n) + abs(e))

print(abs(e2) + abs(n2))
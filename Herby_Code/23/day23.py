inp = '389125467'
#inp = '716892543'
cups = [*map(int, list(inp))]

#print(cups)

current_i = 0
N = len(cups)

for i in range(10):
    #print(f'\n\nMove {i+1}\nCups: {cups[:current_i]} ({cups[current_i]}) {cups[current_i+1:]}') #{' '.join(cups[:current_i])}({cups[current_i]}){' '.join(cups[current_i+1:])}
    picked = cups[current_i+1 : current_i+4]
    cups = cups[:current_i+1] + cups[current_i+4:]

    next_label = cups[current_i + 1]
    dest_label = cups[current_i] - 1


    if dest_label < 1: dest_label += N

    while dest_label in picked:
        dest_label -= 1
        if dest_label < 1: dest_label += N
    
    dest_i = cups.index(dest_label)
    
    #print(f'Picked up {picked}\ndest_label {dest_label}, dest_i {dest_i}')

    cups = cups[:dest_i+1] + picked + cups[dest_i+1:]

    current_i = cups.index(next_label)

    cups = cups[current_i:] + cups[:current_i]
    current_i = 0
    #current_i = (current_i + 1) % N

#print('Final', cups)

one_i = cups.index(1)
cups = cups[one_i+1:] + cups[:one_i]
#print('Silver:', ''.join(map(str, cups)))

# Part 2

cups = [*map(int, list(inp))]
t = 100 # 1_000_000
cups += list(range(max(cups) + 1, t + 1))

N = len(cups)
print(N)
print(N == t)

#current_i = 0
for i in range(10 * t): #10_000_000

    if i % t == 0:
        print(str(i).rjust(3), str(cups[1] * cups[2]).rjust(4), cups[:10])
    #print(str(i).rjust(3), str(cups[1]).ljust(3), str(cups[2]).ljust(3))
    #input()

    picked = cups[1 : 4]
    #cups = [cups[0]] + cups[4:]

    dest_label = cups[0] - 1

    if dest_label < 1: dest_label += N

    while dest_label in cups[1:4]:
        dest_label -= 1
        if dest_label < 1: dest_label += N
    
    dest_i = cups.index(dest_label)

    """cups = cups[:dest_i+1] + picked + cups[dest_i+1:]

    if current_i + 1 < dest_i + 1:
        pass
    else:
        current_i += 3
    
    cups = cups[current_i:] + cups[:current_i]
    current_i = 0"""
    #print(cups, dest_i)
    cups = cups[4 : dest_i + 1] + cups[1:4] + cups[dest_i+1:] + [cups[0]]

print(cups[1]*cups[2], cups[:10])
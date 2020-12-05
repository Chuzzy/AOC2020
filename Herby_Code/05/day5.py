def bin_to_dec(bin):
    #print([(2**i, int(a)) for i, a in enumerate(bin[::-1])])
    return sum(2**i*int(a) for i, a in enumerate(bin[::-1]))

def seat(bp):
    return (sum(2**i * (a == 'B') for i, a in enumerate(bp[0:7][::-1])),\
            sum(2**j * (b == 'R') for j, b in enumerate(bp[7:10][::-1])))

def seat_id(seat):
    return seat[0] * 8 + seat[1]

with open('input5.txt', 'r') as file:
    inp = [*map(lambda x: x.strip(), file.readlines())]

#print([(seat(i), seat_id(seat(i))) for i in ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']])

print('Silver:', max(seat_id(seat(i)) for i in inp))

seats = {seat_id(seat(i)): seat(i) for i in inp}
sorted_ids = sorted(seats.keys())


#print(diffs.index(-2, 2))
for j in range(sorted_ids[0], sorted_ids[-1]):
    if j not in sorted_ids:
        print(j)
        break
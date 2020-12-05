with open('input5.txt', 'r') as file:
    #inp = [l.strip() for l in file.readlines()]
    inp = file.read().splitlines()

def seat_id(bp):
    """Replace FBRL -> 1010 and convert binary to decimal""" 
    return int(bp.replace('F', '0').replace('B', '1') \
                .replace('R', '1').replace('L', '0'), 2)

ids = sorted(map(seat_id, inp))
print('Silver:', ids[-1])

#for j in range(ids[0], ids[-1]):
#    if j not in ids:
#        print('Gold:', j)
#        break

j = ids[0]
while j in ids: j += 1
print('Gold:', j)
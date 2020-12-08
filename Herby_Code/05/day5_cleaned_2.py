with open('input5.txt', 'r') as file:
    #inp = [l.strip() for l in file.readlines()]
    inp = file.read().splitlines()

def seat_id(bp):
    """Replace FBRL -> 1010 and convert binary to decimal""" 
    return int(bp.replace('F', '0').replace('B', '1') \
                .replace('R', '1').replace('L', '0'), 2)

ids = [*map(seat_id, inp)]
big = max(ids)
print('Silver:', big)

j = big - len(ids)
while j in ids: j += 1
print('Gold:', j)
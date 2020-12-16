with open('input15.txt', 'r') as file:
    inp = [int(x) for x in file.read().split(',')]

inp = [0, 3, 6]

*start, prev = inp
last_seen = {x: i for i, x in enumerate(start)}
#print(last_seen)
from copy import copy

for i in range(len(start), 30_000_000 - 1): # 

    if prev in last_seen.keys():
        temp = prev
        prev = i - last_seen[prev]
        last_seen[temp] = i
    else:
        last_seen[prev] = i
        prev = 0
    
    if i + 2 == 2020:
        print('mid', prev)

print('end', prev)

# correct == [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]
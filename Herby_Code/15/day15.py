inp = 17,1,3,16,19,0
inp = 0, 3, 6

start = [int(i) for i in inp]

from copy import copy
said = copy(start)

for i in range(len(start), 2020):
    if said[-1] in said[:-1]:
        said.append(i - (len(said) - 1 - said[:-1][::-1].index(said[-1])))
    else:
        said.append(0)


print(said[2019])
print(said[:20])

said = [17,1,3,16,19,0]
#said = [0,3,6]
last = {x: i for i, x in enumerate(said[:-1])}

for i in range(len(said), 30000000):
    #print('\n\ni', i, 'said', said, '\nlast', last)
    if said[-1] in last.keys():
        t = i - last[said[-1]] - 1
        #print('adding', said[-1], t)
        last[said[-1]] = i - 1
        said.append(t)
    else:
        #print('notseen', said[-1], 0)
        last[said[-1]] = i - 1
        said.append(0)

print(said[30000000-1])
#from math import pow

card_pub = 14222596
door_pub = 4057428

def transform(sub, loop):
    return pow(sub, loop, 20201227)

#print(transform(7, 8))

card_loop = 0
while transform(7, card_loop) != card_pub:
    card_loop += 1

door_loop = 0
while transform(7, door_loop) != door_pub:
    door_loop += 1


print(card_loop, door_loop)
print(transform(7, card_loop))
print(transform(7, door_loop))

print(transform(card_pub, door_loop))
print(transform(door_pub, card_loop))
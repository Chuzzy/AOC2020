from time import time

with open('input7.txt', 'r') as file:
    inp = file.read().splitlines()

bags = dict()

for line in inp:
    outer, inner = line[:-1].split(' contain ')
    outer = outer[:-5]

    if inner == 'no other bags':
        bags[outer] = None
    else:
        parse = lambda b: (int(b[0]), " ".join(b[1:3]))
        inner = [parse(i.split(' ')) for i in inner.split(', ')]
        bags[outer] = inner

contains_gold = {'shiny gold': True}

def bag_containers(bag):
    if bag in contains_gold.keys():
        return contains_gold[bag]
    if bags[bag] == None:
        return False

    contains_gold[bag] = any(bag_containers(bag2) for _, bag2 in bags[bag])
    return contains_gold[bag]

for bag in bags:
    bag_containers(bag)

bags_inside = {}

def count_inside(bag):
    if bag in bags_inside.keys():
        return bags_inside[bag]
    elif bags[bag] == None:
        return 1
    
    return 1 + sum(j * count_inside(bag2) for j, bag2 in bags[bag])

now = time()
print('Silver:', sum(contains_gold.values()) - 1)
print('Gold:', count_inside('shiny gold') - 1)
print('Time:', time() - now)
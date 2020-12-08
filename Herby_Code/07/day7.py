with open('input7.txt', 'r') as file:
    inp = file.read().splitlines()

bags = dict()

for line in inp:
    # Remove final space + split first and second parts
    outer, inner = line[:-1].split(' contain ')
    # Remove 'bags' from first part
    outer = outer[:-5]

    if inner == 'no other bags':
        bags[outer] = None
    else:
        parse = lambda b: (int(b[0]), " ".join(b[1:3]))
        inner = [parse(i.split(' ')) for i in inner.split(', ')]
        bags[outer] = inner


def contains_gold(outer, cont):
    if cont[outer] == None:
        return False

    if 'shiny gold' in map(lambda x: x[1], cont[outer]):
        return True

    return any(contains_gold(j, cont) for j in map(lambda x: x[1], cont[outer]))

def count_inside(bag, cont):
    if cont[bag] == None:
        return 1

    return 1 + sum(j * count_inside(b, cont) for j, b in cont[bag])

gold_count = 0

for outer, inner in bags.items():
    gold_count += contains_gold(outer, bags)

print('Part 1:', gold_count)
print('Part 2:', count_inside('shiny gold', bags) - 1)
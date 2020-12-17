sample = [x.splitlines() for x in """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".split('\n\n')]

inp = [x.splitlines() for x in open('input16.txt').read().split('\n\n')]

rules, your_ticket, other_tickets = inp

parse_rule = lambda rl: (int((s := rl.split('-'))[0]), int(s[1]))
#print(parse_rule('1-3'))

rules = {(s := x.split(': '))[0]: [parse_rule(t) for t in s[1].split(' or ')] for x in rules}
#print(rules)

parse_ticket = lambda tc: [int(x) for x in tc.split(',')]

your_ticket = parse_ticket(your_ticket[1])
other_tickets = [parse_ticket(tc) for tc in other_tickets[1:]]

#print(your_ticket)
#print(other_tickets)

def valid(field, rule):
    return any(rl[0] <= field <= rl[1] for rl in rule)

part1 = 0
#for ticket in other_tickets:
#    part1 += all(any(valid(field, rl) for rl in rules.values()) for field in ticket)

for ticket in other_tickets:
    for field in ticket:
        if not any(valid(field, rl) for rl in rules.values()):
            part1 += field

print('Silver:', part1)

valid_ticket = lambda ticket: all(any(valid(field, rl) for rl in rules.values()) for field in ticket)

valid_tickets = list(filter(valid_ticket, other_tickets))

possibilities = [set(rules.keys()) for _ in range(len(your_ticket))]
finals = [None] * len(your_ticket)
for ticket in valid_tickets:
    for i, field in enumerate(ticket):
        possible_fields = {k for k, v in rules.items() if valid(field, v)}
        possibilities[i].intersection_update(possible_fields)

#print(possibilities)
while any(f == None for f in finals):
    for i in range(len(finals)):
        if len(possibilities[i]) == 1:
            for j in range(len(finals)):
                if j != i:
                    possibilities[j].difference_update(possibilities[i])
            
            finals[i] = possibilities[i].pop()

#print(finals)

from math import prod
print('Gold:', prod(f for i, f in enumerate(your_ticket) if finals[i][:len('departure')] == 'departure'))

#print([(f, finals[i]) for i, f in enumerate(your_ticket)])
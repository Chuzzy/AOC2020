
class Node():
    def __init__(self, val, nex):
        self.next = nex
        self.val = val
    
    def __str__(self):
        node = self
        result = str(node.val) + ' '

        while node.next != None and node.next != self:
            node = node.next
            result += str(node.val) + ' '
        
        return result[:-1]
    
    def __repr__(self):
        return f'Node, val: {self.val}' #, next: {self.next}

inp = '389125467'
inp = '716892543'
cups = [*map(int, list(inp))]

t = 1_000_000
cups += list(range(max(cups) + 1, t + 1))
N = len(cups)
print(N)

xs = Node(cups[0], None)
pos = [None] * (N + 1)
pos[cups[0]] = xs

node = xs

for x in cups[1:]:
    node.next = Node(None, None)
    node = node.next
    node.val = x
    pos[x] = node


#print(xs)
#print(pos)

pos[cups[-1]].next = pos[cups[0]]

current = pos[cups[0]]
#print(current.next)
#print(current.next.next)

for i in range(10 * t):
    picked = [current.next, current.next.next, current.next.next.next]
    picked_vals = [*map(lambda x: x.val, picked)]
    
    target = current.val - 1

    if target < 1: target += N

    while target in picked_vals:
        #print(target)
        target -= 1
        if target < 1: target += N
    
    next_current = current.next.next.next.next

    current.next = next_current


    new_target = pos[target]

    picked[2].next = new_target.next
    new_target.next = picked[0]

    current = next_current

#print(xs)

print(pos[1].next.val, pos[1].next.next.val)
print(pos[1].next.val * pos[1].next.next.val)
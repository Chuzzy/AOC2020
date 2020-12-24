def part1_(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 > card2:
            player1 += [card1, card2] 
        else:
            player2 += [card2, card1]

    return max(player1, player2)

def part1(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        t = [p1.pop(0), p2.pop(0)]
        [p2, p1][t[0] > t[1]] += sorted(t)[::-1]
    
    return max(p1, p2)

def part2(p1, p2):
    seen = set()

    while len(p1) > 0 and len(p2) > 0:
        if (tuple(p1), tuple(p2)) in seen:
            return True, p1

        seen.add((tuple(p1), tuple(p2)))
        c1, c2 = p1.pop(0), p2.pop(0)

        if c1 > len(p1) or c2 > len(p2):
            [p2, p1][c1 > c2] += [[c2, c1], [c1, c2]][c1 > c2]
        else:
            w, _ = part2(p1[:c1], p2[:c2])

            [p2, p1][w] += [[c2, c1], [c1, c2]][w]

    return p1 > p2, max(p1, p2)

parse = lambda p: list(map(int, p.splitlines()[1:]))
player1, player2 = [parse(p) for p in open('input22.txt').read().split('\n\n')]

score = lambda deck: sum( (i+1) * x for i, x in enumerate(deck[::-1]))

print('Silver:', score(part1(player1[:], player2[:])))
_, deck = part2(player1, player2)
print('Gold:', score(deck))
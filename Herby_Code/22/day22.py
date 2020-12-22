from copy import copy
player1, player2 = [9, 2, 6, 3, 1], [5, 8, 4, 7, 10]

with open('input22.txt', 'r') as file:
    player1, player2 = file.read().split('\n\n')

parse = lambda p: list(map(int, p.splitlines()[1:]))
player1, player2 = parse(player1), parse(player2)


score = lambda deck: sum( (i+1) * x for i, x in enumerate(deck[::-1]))

def part1(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 > card2: 
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    return max(player1, player2)

print('Silver:', score(part1(player1[:], player2[:])))

def part2(p1, p2):
    """Returns (True for p1/False for p2, winning deck)"""
    seen = set()

    while len(p1) > 0 and len(p2) > 0:
        #print(f'\n\nPlayer 1\'s deck: {p1}\nPlayer 2\'s deck: {p2}')
        if (tuple(p1), tuple(p2)) in seen:
            # p1 wins
            #print(f'Player 1 wins game by repeated state with deck {p1}')
            return True, p1

        seen.add((tuple(p1), tuple(p2)))

        c1, c2 = p1.pop(0), p2.pop(0)

        #print(f'Player 1 card: {c1}\nPlayer 2 card: {c2}')

        if c1 > len(p1) or c2 > len(p2):
            # end of round
            #print(f'Player {2-int(c1 > c2)} wins round with deck {[p1, p2][c1 < c2]}')
            if c1 > c2:
                #print(f'Player 1 wins with deck {p1}')
                p1.append(c1)
                p1.append(c2)
            else:
                #print(f'Player 2 wins with deck {p2}')
                p2.append(c2)
                p2.append(c1)
            #return c1 > c2, p1 if c1 > c2 else p2
            #print(f'Now P1: {p1}, P2: {p2}')
        else:
            # recurse into subgame
            #input()
            #print(f'\nRecursing into subgame where :\nP1 has {p1[:c1]}\nP2 has {p2[:c2]}')
            w, _ = part2(copy(p1[:c1]), copy(p2[:c2]))

            if w:
                #print(f'P1 wins subgame')
                # p1 wins subgame
                p1.append(c1)
                p1.append(c2)
                #print(f'P1 now has: {p1}\nP2 has: {p2}')
            else:
                #print(f'P2 wins subgame')
                # p2 wins subgame
                p2.append(c2)
                p2.append(c1)
                #print(f'P2 now has: {p2}\nP1 has: {p1}')
        #input()

    # End of the game
    #print(f'Player {2-int(p1 > p2)} wins')    
    return p1 > p2, max(p1, p2)

_, deck = part2(player1, player2)
print('Gold:', score(deck))
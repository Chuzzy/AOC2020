from itertools import product, combinations

def words(rules, initial = 0):
    if type(rules[initial]) == str:
        return [rules[initial]]

    return [''.join(w) for rule_list in rules[initial] for w in product(*list(words(rules, r) for r in rule_list))]


def subwords(word):
    """Unnecessary, but could be useful later"""
    for i in range(len(word)):
        for c in combinations(range(1, len(word)), r = i):
            yield [word[x:y] for x, y in zip((0,) + c, c + (len(word),))]
        

def valid_subwords(word, allowed_words, len_ = 0):
    # Check whether some 'splitting' of
    # a word has all subwords in allowed_words
    if word in allowed_words: return (True, 1)

    for i in range(len(word)):
        if word[:i] in allowed_words:
            valid, len_ = valid_subwords(word[i:], allowed_words, len_ = len_ + 1)
            
            if valid: return (True, len_ + 1)
    
    return (False, 0)

rules_raw, received = open('input19.txt', 'r').read().split('\n\n')
rules, received = {}, received.splitlines()

for line in rules_raw.splitlines():
    num, rule_list = line.split(': ')

    if rule_list[0] == '\"':
        rules[int(num)] = rule_list[1]
    else:
        rules[int(num)] = [tuple(map(int, x.split(' '))) for x in rule_list.split(' | ')]

words_0  = set(words(rules, 0))
words_42 = set(words(rules, 42))
words_31 = set(words(rules, 31))

part1 = part2 = 0

for word in received:
    part1 += word in words_0
    valid = False

    for i in range(len(word)):
        l_valid, l_len = valid_subwords(word[:i], words_42)
        r_valid, r_len = valid_subwords(word[i:], words_31)

        if l_valid and r_valid and l_len > r_len:
            part2 += 1
            break

print('Silver:', part1)
print('Gold:', part2)
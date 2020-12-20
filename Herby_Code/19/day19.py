from copy import copy
from itertools import product, combinations, chain

def words(rules, initial = 0):
    #print(f'Doing rule {initial}: {rules[initial]}')
    results = []

    if type(rules[initial]) == str:
        #print(f'Simple rule, returing: {rules[initial]}\n')
        return [rules[initial]]
    
    for rule_list in rules[initial]:
        new = []

        for w in product(*list(words(rules, r) for r in rule_list)):
            #print(f'w: {w}')
            #print('Actual word:', ''.join(w))

            new.append(''.join(w))

        results += new

        #new_words = [''.join(w) for w in product(words(rules, r) for r in rule_list)]
        #results.append(new_words)

    #print(f'Final results: {results}\n')
    return results

def match(word, rules, initial = 0):
    if type(rules[initial]) == str:
        return rules[initial] == word
    

    for rule_list in rules[initial]:
        for i in range(len(word)):
            if len(rule_list) == 1:
                return match(word, rules, rule_list[0])

            if match(word[:i], rules, initial = rule_list[0]):
                if i + 1 == len(word): return True
                newrules = copy(rules)
                newrules[max(rules.keys()) + 1] = [rule_list[1:]]
                return match(word[i:], newrules, max(rules.keys()) + 1)
    
    # No match
    #print(initial, rules[initial], word)
    return False

def subwords(word):
    for i in range(0, len(word)):
        for combo in combinations(range(1, len(word)), r = i):
            combo2 = [0] + list(combo) + [len(word)]
            sl = zip(combo2, combo2[1:])

            #print(i, combo, list(sl))
            #for x, y in sl:
            #    print(word[x:y], end = ' ')
            
            #print([word[x:y] for x, y in sl])
            yield [word[x:y] for x, y in sl]


def splitter(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result



def valid_subwords(word, allowed_words):
    for subs in subwords(word):
        #if all(w in allowed_words for w in subs):
        #    return (True, len(subs))
        ok = True
        for sub in subs:
            if sub not in allowed_words:
                ok = False
                break
        
        if not ok: continue
    
        return (True, len(subs))

    return (False, 0)

def valid_subwords_2(word, allowed_words, len_ = 0):
    if word in allowed_words: return (True, 1)

    for i in range(len(word)):
        if word[:i] in allowed_words:
            x, y = valid_subwords_2(word[i:], allowed_words, len_ = len_ + 1)
            
            if x:
                return (True, y + 1)
    
    return (False, 0)

rules = {
        0: [(4, 1, 5)],
        1: [(2, 3), (3, 2)],
        2: [(4, 4), (5, 5)],
        3: [(4, 5), (5, 4)],
        4: 'a',
        5: 'b'
        }

received = """ababbb
bababa
abbbab
aaabbb
aaaabbb""".splitlines()

rules_raw, received = open('input19.txt', 'r').read().split('\n\n')

for line in rules_raw.splitlines():
    num, rule_list = line.split(': ')

    if rule_list[0] == '\"':
        rules[int(num)] = rule_list[1]
    else:
        rules[int(num)] = [tuple(map(int, x.split(' '))) for x in rule_list.split(' | ')]

received = received.splitlines()

print(len(set(words(rules, 0)) & set(received)))

words_42 = set(words(rules, 42))
words_31 = set(words(rules, 31))



"""
test_word = 'bbabbbbaabaabba'
print(test_word in words_42, test_word in words_31)

for i in range(len(test_word)):
    print(i, test_word[:i], test_word[i:])
    print(valid_subwords_2(test_word[:i], words_42), valid_subwords_2(test_word[i:], words_31))
    print()
#exit()
"""

valid_count = 0
valid_words = set()

for word in received:
    valid = False
    # Rule 0: 8 11
    # So match first part of word to 8 and second part to 11
    
    t = 0

    #for i in range(len(word)):
    while t <= len(word) and not valid:
        #print('\n', t, 'Parts:', word[:t], 'and', word[t:])
        
        l_valid, l_len = valid_subwords_2(word[:t], words_42)

        if not l_valid:
            #print('Not l_valid')
            t += 1
            continue

        #print('l_valid', word[:t], word[t:])
        #print(valid_subwords_2(word[t:], words_31))
        r_valid, r_len = valid_subwords_2(word[t:], words_31)

        #print(r_valid, r_len)

        """if not lvalid:
            t += 1
            continue

        print(lvalid, 'Continuing to 11 part')

        for subs in subwords(word[t:]):
            #print('rhs subs:', subs)
            if all(x in words_31 for x in subs):
                rvalid = True
                r_len = len(subs)
                break"""

        if l_valid and r_valid and l_len > r_len:
            valid = True
            break

        t += 1


            
    if valid:
        valid_count += 1
        valid_words.add(word)
        print(word)

print(valid_words)
print(valid_count)
print(len(valid_words))
def eval_expr(expr):
    if len(expr) == 1:
        return int(expr[0])
    
    if expr[-2] == '+':
        return int(expr[-1]) + eval_expr(expr[:-2])
    elif expr[-2] == '*':
        return int(expr[-1]) * eval_expr(expr[:-2])
    elif expr[-1] == ')':
        #print('expr', expr)
        t = len(expr) - 1
        seen_rb = 0
        #print('t initial', t)
        while expr[t] != '(' or seen_rb > 1:
            #print('t', t, seen_rb, expr[t])
            if expr[t] == ')': seen_rb += 1
            if expr[t] == '(': seen_rb -= 1
            t -= 1

        if t == 0:
            return eval_expr(expr[t+1:-1])
        if expr[t-1] == '+':
            return eval_expr(expr[:t-1]) + eval_expr(expr[t+1:-1])
        elif expr[t-1] == '*':
            return eval_expr(expr[:t-1]) * eval_expr(expr[t+1:-1])

        print('ALERT ALERT WHAT IS GOING ON')
        print(t)
        print(expr[-1] == ')')
        print(expr)


def eval_expr_2(expr):
    #print('Start', show(expr))
    if len(expr) == 1:
        #print(expr)
        return int(expr[0])
    
    if len(expr) == 3:
        if expr[1] == '+':
            return int(expr[0]) + int(expr[2])
        elif expr[1] == '*':
            return int(expr[0]) * int(expr[2])

    for i, x in enumerate(expr):
        if x == '(': # expr[i] == '('
            num = 0
            for j, y in enumerate(expr[i:]):
                if y == '(': num += 1
                if y == ')': num -= 1
                
                if y == ')' and num == 0: # expr[j] == ')'
                    #print('i; i+j', i, +j)
                    expr = expr[:i] + [eval_expr_2(expr[i + 1:i + j])] + expr[i + j + 1:]
                    #print('Broken', show(expr))
                    return eval_expr_2(expr)
            
            print('THIS SHOULDN\'T HAPPEN', show(expr))

    """if expr[0] == '(':
        num = 0
        for i, x in enumerate(expr):
            if x == '(': num += 1
            if x == ')' and num == 0:
                return [eval_expr_2(expr[1:i-1])] + expr[i:]
            elif x == ')':
                num -= 1"""

    # Should have no brackets
    #print(expr)
    if '*' in expr:
        #return prod(eval_expr_2(e) for e in split_list(expr, '*'))
        return prod(eval_expr_2(e) for e in split_list(expr, '*'))
    else:
        #print('ERROR ERROR STOP')
        #print(show(expr))
        #raise(NotImplementedError)
        #print(show(expr))
        return sum(int(e.pop()) for e in split_list(expr, '+'))



show = lambda xs: " ".join(map(str, xs))

def parse(txt):
    return list(txt.replace(' ', '').strip('\n'))


def split_list(xs, char):
    left = -1
    for i, x in enumerate(xs):
        if x == char:
            yield xs[left + 1:i]
            left = i
    
    yield xs[left + 1:]

from math import prod

def get_bracket(expr):
    for i, x in enumerate(expr):
        pass

def parse2(expr):
    for sub in split_list(expr, '*'):
        print(sub)
    if '*' not in expr:
        print(show(expr))
        return 0

    print(expr, 'WHY?')
    return prod(parse2(sub) for sub in split_list(expr, '*'))

inp = open('input18.txt', 'r').readlines()
#for l in inp:
#    print(parse(l))
#    print(eval_expr(parse(l)))

print('Silver:', sum(eval_expr(parse(l)) for l in inp))
print('Gold:', sum(eval_expr_2(parse(l)) for l in inp))
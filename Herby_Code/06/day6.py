with open('input6.txt', 'r') as file:
    passes = [p for p in file.read().split('\n\n')]

print(sum(len(set(p.replace('\n', ''))) for p in passes))

passes = [p.split() for p in passes]

print(sum(len(set(p[0]).intersection(*map(set, p))) for p in passes))
#print([[set(p[0]).intersection(*map(set, p))] for p in passes[:5]])
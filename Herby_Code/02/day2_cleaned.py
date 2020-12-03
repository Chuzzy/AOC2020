part1 = part2 = 0

for line in open("input2.txt", 'r'):
    ns, ch, pwd = line.split(' ')
    n, m = map(int, ns.split('-'))

    part1 += n <= pwd.count(ch[0]) <= m
    part2 += (pwd[n-1] == ch[0]) != (pwd[m-1] == ch[0])
    #if n <= pwd.count(ch[0]) <= m: part1 += 1
    #if (pwd[n-1] == ch[0]) != (pwd[m-1] == ch[0]): part2 += 1

print("Silver:", part1)
print("Gold:", part2)
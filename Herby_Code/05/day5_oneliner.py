print((lambda x:f'Part 1: {max(x)}\nPart 2: {min(set(range(min(x),max(x)))-set(x))}')([int("".join(str(int(x in 'BR')) for x in l[:-1]),2) for l in open('input5.txt').readlines()]))

def bin(xs):
    return(int("".join(str(int(x in 'BR')) for x in xs[:-1]),2))

def bin2(xs):
    return(int(xs.replace('F','0').replace('B','1').replace('R','1').replace('L','0'),2))

print(bin('BBFFFFBLRL\n'))
print(bin2('BBFFFFBLRL\n'))

print(max([(int(line.strip('\n').replace('F', '0').replace('B','1').replace('L', '0').replace('R', '1')[:7], 2)*8+int(line.strip('\n').replace('F', '0').replace('B','1').replace('L', '0').replace('R', '1')[7:], 2)) for line in open('input5.txt', 'r')]), '\n', [i+1 for index, i in enumerate(sorted([(int(line.strip('\n').replace('F', '0').replace('B','1').replace('L', '0').replace('R', '1')[:7], 2)*8+int(line.strip('\n').replace('F', '0').replace('B','1').replace('L', '0').replace('R', '1')[7:], 2)) for line in open('input5.txt', 'r')])[:-1]) if i+1!=sorted([(int(line.strip('\n').replace('F', '0').replace('B','1').replace('L', '0').replace('R', '1')[:7], 2)*8+int(line.strip('\n').replace('F', '0').replace('B','1').replace('L', '0').replace('R', '1')[7:], 2)) for line in open('input5.txt', 'r')])[index+1]][0])

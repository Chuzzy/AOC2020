report = map(int, """1721
979
366
299
675
1456""".split('\n'))

with open("input1.txt", 'r') as file:
    report = list(map(int, file.read().split('\n')[:-1]))

#print(report)

for num in report:
    for num2 in report:
        if num + num2 == 2020:
            print("Part 1: ", num*num2)

for num in report:
    for num1 in report:
        for num2 in report:
            if num + num1 + num2 == 2020:
                print("Part 2:", num*num1*num2)
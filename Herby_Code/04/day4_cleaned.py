from re import fullmatch

def valid_passport(psp):
    date = lambda n, m, f: len(f) == 4 and n <= int(f) <= m
    byr = date(1920, 2002, psp['byr'])
    iyr = date(2010, 2020, psp['iyr'])
    eyr = date(2020, 2030, psp['eyr'])

    hgt = psp['hgt'][-2:] == 'cm' and 150 <= int(psp['hgt'][:-2]) <= 193 \
        or psp['hgt'][-2:] == 'in' and 59 <= int(psp['hgt'][:-2]) <= 76

    hcl = fullmatch(r'#[a-z0-9]{6}', psp['hcl']) != None
    ecl = psp['ecl'] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    pid = fullmatch(r'[0-9]{9}', psp['pid']) != None

    return byr and iyr and eyr and hgt and hcl and ecl and pid

inp = [*map(lambda x: x.split(), open('input4.txt', 'r').read().split('\n\n'))]

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} # 'cid' optional
part1 = part2 = 0

for p in inp:
    pc = {(s := f.split(':'))[0]: s[1] for f in p}

    if required.intersection(pc.keys()) == required:
        part1 += 1
        part2 += valid_passport(pc)

print('Silver:', part1, '\nGold', part2)
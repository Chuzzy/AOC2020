inp = [*map(lambda x: x.split(), """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split('\n\n'))]


def valid_passport(passport):
    byr = len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002
    iyr = len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020
    eyr = len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030
    if passport['hgt'][-2:] == 'cm':
        hgt = 150 <= int(passport['hgt'][:-2]) <= 193
    elif passport['hgt'][-2:] == 'in':
        hgt = 59 <= int(passport['hgt'][:-2]) <= 76
    else:
        hgt = False
    hcl = (passport['hcl'][0] == '#') and set(passport['hcl'][1:]).issubset(set("abcdef0123456789"))
    ecl = passport['ecl'] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    pid = len(passport['pid']) == 9 and set(passport['pid']).issubset(set("0123456789"))

    #print(byr, iyr, eyr, hgt, hcl, ecl, pid)
    return byr and iyr and eyr and hgt and hcl and ecl and pid
    

inp = [*map(lambda x: x.split(), open('input4.txt', 'r').read().split('\n\n'))]

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} # 'cid' optional

part1 = part2 = 0

for passport in inp:
    cleaned = {(s := field.split(':'))[0]: s[1] for field in passport}
    if required.intersection(cleaned.keys()) == required:
        part1 += 1
        part2 += valid_passport(cleaned)

print('Silver:', part1)
print('Gold:', part2)
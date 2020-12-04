import re

def verify_hgt(hgt):
    match = re.search(r'^(\d+)(cm|in)$', hgt)
    if not match:
        return False
    else:
        num, unit = match.groups()
        num = int(num)
        if unit == 'cm':
            return 150 <= num <= 193
        elif unit == 'in':
            return 59 <= num <= 76
        else:
            raise AssertionError("This shouldn't happen")

fields = {
    'byr': lambda byr: 1920 <= int(byr) <= 2002,
    'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
    'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
    'hgt': verify_hgt,
    'hcl': lambda hcl: re.search(r'^#[0-9a-f]{6}$', hcl) is not None,
    'ecl': lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda pid: re.search(r'^[0-9]{9}$', pid) is not None,
    # cid is ignored
}

def validate1(passport):
    return all(field in passport for field in fields)

def validate2(passport):
    return all(fields.get(key, lambda value: True)(value)
               for key, value in passport.items())

with open('input.txt') as f:
    passports = [dict(pair.split(':') for pair in passport.split())
                 for passport in f.read().split('\n\n')]
    passports = list(filter(validate1, passports))
    print(len(passports))
    print(sum(map(validate2, passports)))

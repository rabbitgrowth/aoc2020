import re

def verify_hgt(hgt):
    match = re.match(r'(\d+)(cm|in)', hgt)
    if not match:
        return False
    else:
        num, unit = match.groups()
        num = int(num)
        if unit == 'cm':
            return 150 <= num <= 193
        else:
            return 59 <= num <= 76

fields = {
    'byr': lambda byr: 1920 <= int(byr) <= 2002,
    'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
    'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
    'hgt': verify_hgt,
    'hcl': lambda hcl: re.match(r'#[0-9a-f]{6}$', hcl),
    'ecl': lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda pid: re.match(r'[0-9]{9}$', pid),
    'cid': lambda cid: True,
}

def validate1(passport):
    return all(field in passport for field in fields if field != 'cid')

def validate2(passport):
    return all(fields[key](value) for key, value in passport.items())

with open('input.txt') as f:
    passports = [dict(pair.split(':') for pair in passport.split())
                 for passport in f.read().split('\n\n')]
    valid1 = [passport for passport in passports if validate1(passport)]
    print(len(valid1))
    valid2 = [passport for passport in valid1    if validate2(passport)]
    print(len(valid2))

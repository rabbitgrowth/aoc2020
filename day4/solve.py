fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
fields.remove('cid') # treat country ID as optional

with open('input.txt') as f:
    passports = [dict(pair.split(':') for pair in passport.split())
                 for passport in f.read().split('\n\n')]
    print(sum(set(passport.keys()) >= fields for passport in passports))

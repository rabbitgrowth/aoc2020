def desuffix(bag):
    return bag.removesuffix('s').removesuffix(' bag')

BAGS = {}
with open('input.txt') as f:
    for line in f:
        line = line.removesuffix('.\n')
        before, after = line.split(' contain ')
        bag = desuffix(before)
        subbags = {}
        if after != 'no other bags':
            for item in after.split(', '):
                number, subbag = item.split(maxsplit=1)
                number = int(number)
                subbag = desuffix(subbag)
                subbags[subbag] = number
        BAGS[bag] = subbags

def find_shiny_gold(bag):
    subbags = BAGS[bag]
    if 'shiny gold' in subbags:
        return True
    else:
        return any(find_shiny_gold(subbag) for subbag in subbags)

print(sum(find_shiny_gold(bag) for bag in BAGS))

def desuffix(bag):
    return bag.removesuffix('s').removesuffix(' bag')

BAGS = {}
with open('input.txt') as f:
    for line in f:
        line = line.removesuffix('.\n')
        before, after = line.split(' contain ')
        colour = desuffix(before)
        if after == 'no other bags':
            contains = {}
        else:
            contains = {desuffix(bag.split(maxsplit=1)[1]) # ignore number for now
                        for bag in after.split(', ')}
        BAGS[colour] = contains

def find_shiny_gold(bag):
    subbags = BAGS[bag]
    if 'shiny gold' in subbags:
        return True
    else:
        return any(find_shiny_gold(subbag) for subbag in subbags)

print(sum(find_shiny_gold(bag) for bag in BAGS))

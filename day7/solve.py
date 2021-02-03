import re
from collections import defaultdict

bottom_up = defaultdict(list)
top_down  = defaultdict(list)

with open('input.txt') as f:
    for line in f:
        outer, rhs = line.split(' bags contain ')
        for count, inner in re.findall(r'(\d) (.+?) bag', rhs):
            bottom_up[inner].append(outer)
            top_down[outer].append((int(count), inner))

def possible_outers(bottom_up, bag, seen=set()):
    for outer in bottom_up[bag]:
        if outer not in seen:
            seen.add(outer)
            possible_outers(bottom_up, outer, seen)
    return len(seen)

def total_inners(top_down, bag):
    total = 0
    for count, inner in top_down[bag]:
        total += count
        total += count * total_inners(top_down, inner)
    return total

print(possible_outers(bottom_up, 'shiny gold'))
print(total_inners(top_down, 'shiny gold'))

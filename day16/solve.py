import re
from itertools import chain

def ints(line):
    return tuple(map(int, line.split(',')))

with open('input.txt') as f:
    par1, par2, par3 = f.read().split('\n\n')
    constraints = {}
    for line in par1.splitlines():
        field, rhs = line.split(': ')
        min1, max1, min2, max2 = map(int, re.findall(r'\d+', rhs))
        constraints[field] = (range(min1, max1 + 1), range(min2, max2 + 1))
    mine = ints(par2.splitlines()[1])
    nearby = [ints(line) for line in par3.splitlines()[1:]]

valid_nearby = []
error_rate = 0

for values in nearby:
    error = False
    for value in values:
        if all(value not in range_
               for ranges in constraints.values()
               for range_ in ranges):
            error_rate += value
            error = True
    if not error:
        valid_nearby.append(values)

print(error_rate) # Part 1

rows    = chain((mine,), valid_nearby)
columns = list(zip(*rows))

choices = [{field
            for field, ranges in constraints.items()
            if all(any(value in range_ for range_ in ranges)
                   for value in column)}
           for column in columns]

seen              = set()
translated_fields = []

answer = 1
for index, fields in sorted(enumerate(choices), key=lambda tpl: len(tpl[1])):
    (field,) = fields - seen # only works for this particular input
    seen.add(field)
    if field.startswith('departure'):
        answer *= mine[index]
print(answer) # Part 2

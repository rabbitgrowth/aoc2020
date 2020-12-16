import re
from itertools import chain

with open('input.txt') as f:
    par1, par2, par3 = f.read().split('\n\n')
    constraints = {}
    for line in par1.splitlines():
        field, rhs = line.split(': ')
        min1, max1, min2, max2 = map(int, re.findall(r'\d+', rhs))
        constraints[field] = (range(min1, max1 + 1), range(min2, max2 + 1))
    mine = list(map(int, par2.splitlines()[1].split(',')))
    nearby = [list(map(int, line.split(',')))
              for line in par3.splitlines()[1:]]

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
columns = [list(values) for values in zip(*rows)]

choices = [(index, {field
                    for field, ranges in constraints.items()
                    if all(any(value in range_ for range_ in ranges)
                           for value in column)})
           for index, column in enumerate(columns)]

seen              = set()
translated_fields = []

for index, fields in sorted(choices, key=lambda tpl: len(tpl[1])):
    (field,) = fields - seen # only works for this particular input
    seen.add(field)
    translated_fields.append((index, field))

answer = 1
for index, field in translated_fields:
    if field.startswith('departure'):
        answer *= mine[index]
print(answer) # Part 2

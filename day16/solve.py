import re

constraints, mine, nearby = {}, [], []

with open('input.txt') as f:
    par1, par2, par3 = f.read().split('\n\n')
    for line in par1.splitlines():
        field, rhs = line.split(': ')
        min1, max1, min2, max2 = map(int, re.findall(r'\d+', rhs))
        constraints[field] = (range(min1, max1 + 1), range(min2, max2 + 1))
    for lst, par in ((mine, par2), (nearby, par3)):
        for line in par.splitlines()[1:]:
            lst.append(list(map(int, line.split(','))))

print(sum(value
          for values in nearby
          for value in values
          if all(value not in range_
                 for ranges in constraints.values()
                 for range_ in ranges)))

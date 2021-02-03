import math
from itertools import combinations

with open('input.txt') as f:
    nums = [int(line) for line in f]

for r in (2, 3):
    for combination in combinations(nums, r):
        if sum(combination) == 2020:
            print(math.prod(combination))
            break

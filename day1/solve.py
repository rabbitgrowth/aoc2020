import operator
from functools import reduce
from itertools import combinations

def solve(nums, r):
    for combination in combinations(nums, r):
        if sum(combination) == 2020:
            return reduce(operator.mul, combination)

if __name__ == '__main__':
    with open('input.txt') as f:
        nums = [int(line) for line in f]
        print(solve(nums, 2))
        print(solve(nums, 3))

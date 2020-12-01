from itertools import combinations

def solve(nums):
    for x, y in combinations(nums, 2):
        if x + y == 2020:
            return x * y

if __name__ == '__main__':
    with open('input.txt') as f:
        nums = [int(line) for line in f]
        print(solve(nums))

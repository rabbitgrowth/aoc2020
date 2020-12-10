from collections import Counter

with open('input.txt') as f:
    nums = sorted(int(line) for line in f)

# Connections to outlet and built-in adapter
diffs = Counter([nums[0], 3])

for x, y in zip(nums, nums[1:]):
    diffs[y - x] += 1

print(diffs[1] * diffs[3])

end = nums[-1]
numset = set(nums)
memo = {}

def ways(num):
    if num in memo:
        return memo[num]
    children = [child
                for i in [1, 2, 3]
                if (child := num + i) in numset]
    result = ((num == end)
              + sum(ways(child) for child in children))
    memo[num] = result
    return result

print(ways(0))

from collections import Counter

with open('input.txt') as f:
    nums = sorted(int(line) for line in f)

smallest = min(nums)

# Connections to outlet and built-in adapter
diffs = Counter([smallest, 3])

for x, y in zip(nums, nums[1:]):
    diffs[y - x] += 1

print(diffs[1] * diffs[3])

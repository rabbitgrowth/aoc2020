from collections import deque
from itertools import combinations

maxlen = 25

with open('input.txt') as f:
    nums = [int(line) for line in f]

it = iter(nums)
queue = deque(maxlen=maxlen)
for _ in range(maxlen):
    queue.append(next(it))
for num in it:
    if any(x + y == num for x, y in combinations(queue, 2)):
        queue.append(num)
    else:
        invalid = num
        break

print(invalid)

for i, start in enumerate(nums):
    total, smallest, largest = start, start, start
    found = False
    for end in nums[i + 1:]:
        total += end
        if end < smallest:
            smallest = end
        if end > largest:
            largest = end
        if total == invalid:
            weakness = smallest + largest
            found = True
            break
        elif total > invalid:
            break

print(weakness)

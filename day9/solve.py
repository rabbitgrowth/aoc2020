from collections import deque
from itertools import combinations

with open('input.txt') as f:
    nums = list(map(int, f))

queue = deque(nums[:25], maxlen=25)

for num in nums[25:]:
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
        elif end > largest:
            largest = end
        if total == invalid:
            weakness = smallest + largest
            found = True
            break
        elif total > invalid:
            break
    if found:
        break

print(weakness)

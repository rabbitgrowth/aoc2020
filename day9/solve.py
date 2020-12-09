from collections import deque
from itertools import combinations

maxlen = 25

with open('input.txt') as f:
    nums = (int(line) for line in f)
    queue = deque(maxlen=maxlen)
    for _ in range(maxlen):
        queue.append(next(nums))
    for num in nums:
        if any(x + y == num for x, y in combinations(queue, 2)):
            queue.append(num)
        else:
            print(num)
            break

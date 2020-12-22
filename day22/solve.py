from collections import deque
from itertools   import count

with open('input.txt') as f:
    p1, p2 = (deque(map(int, par.splitlines()[1:]))
              for par in f.read().split('\n\n'))

while p1 and p2:
    c1, c2 = p1.popleft(), p2.popleft()
    assert c1 != c2
    if c1 > c2:
        p1.extend((c1, c2))
    else:
        p2.extend((c2, c1))

winner = p1 if p1 else p2

print(sum(card * multiplier
          for card, multiplier in zip(winner, count(len(winner), -1))))

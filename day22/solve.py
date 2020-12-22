from collections import deque
from copy        import copy
from itertools   import count, islice

def combat(p1, p2): # -> whether P1 wins
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        assert c1 != c2
        if c1 > c2:
            p1.extend((c1, c2))
        else:
            p2.extend((c2, c1))
    return bool(p1)

def recursive_combat(p1, p2):
    seen = set()
    while p1 and p2:
        decks = tuple(map(tuple, (p1, p2)))
        if decks in seen:
            return True # P1 wins, otherwise game goes on forever
        c1, c2 = p1.popleft(), p2.popleft()
        assert c1 != c2
        seen.add(decks)
        if len(p1) >= c1 and len(p2) >= c2:
            # Recurse into subgame
            p1_copy = deque(islice(p1, c1))
            p2_copy = deque(islice(p2, c2))
            p1_wins = recursive_combat(p1_copy, p2_copy)
        else:
            p1_wins = c1 > c2
        if p1_wins:
            p1.extend((c1, c2))
        else:
            p2.extend((c2, c1))
    return bool(p1)

with open('input.txt') as f:
    l1, l2 = (list(map(int, par.splitlines()[1:]))
              for par in f.read().split('\n\n'))
    for play in (combat, recursive_combat):
        p1, p2 = deque(l1), deque(l2)
        p1_wins = play(p1, p2)
        winner = p1 if p1_wins else p2
        print(sum(card * multiplier
                  for card, multiplier in zip(p1, count(len(p1), -1))))

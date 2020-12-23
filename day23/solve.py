from itertools import chain

with open('input.txt') as f:
    cups = list(map(int, f.read().strip()))

curr_idx = 0

for move in range(100):
    curr = cups[curr_idx]
    pick_idx = curr_idx + 1
    picks = []
    for offset in range(1, 4):
        try:
            picks.append(cups.pop(pick_idx))
        except IndexError:
            picks.append(cups.pop(0))
    try:
        dest = max(cup for cup in cups if cup < curr)
    except ValueError:
        dest = max(cups)
    dest_idx = cups.index(dest)
    for pick in reversed(picks):
        cups.insert(dest_idx + 1, pick)
    curr_idx = (cups.index(curr) + 1) % len(cups)

print(''.join(map(str, chain(cups[cups.index(1)+1:],
                             cups[:cups.index(1)]))))

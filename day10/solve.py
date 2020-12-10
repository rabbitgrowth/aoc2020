from collections import Counter

diffs = Counter()

with open('input.txt') as f:
    ints = [0]
    ints.extend(sorted(int(line) for line in f))
    ints.append(max(ints) + 3)

for x, y in zip(ints, ints[1:]):
    diffs[y - x] += 1

print(diffs[1] * diffs[3])

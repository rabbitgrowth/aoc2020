from collections import Counter

with open('input.txt') as f:
    xs = sorted(int(line) for line in f)

start, end = xs[0], xs[-1]

diffs = Counter([start, 3]) # connections to outlet and built-in adapter
diffs.update(y - x for x, y in zip(xs, xs[1:]))

print(diffs[1] * diffs[3])

xset = set(xs)
memo = {}

def paths(x):
    try:
        return memo[x]
    except KeyError:
        ys = (y for y in range(x + 1, x + 4) if y in xset)
        result = (x == end) + sum(paths(child) for child in ys)
        memo[x] = result
        return result

print(paths(0))

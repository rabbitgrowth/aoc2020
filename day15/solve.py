from itertools import count

INPUT = [12, 20, 0, 6, 1, 17, 7]

haystack = dict(zip(INPUT[:-1], count(1)))
needle   = INPUT[-1]

for turn in range(len(INPUT), 30_000_000):
    try:
        index = haystack[needle]
    except KeyError:
        number = 0
    else:
        number = turn - index
    haystack[needle] = turn
    needle = number

print(number)

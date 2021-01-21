INPUT = [12, 20, 0, 6, 1, 17, 7]

haystack = {n: turn for turn, n in enumerate(INPUT[:-1], 1)}
needle   = INPUT[-1]

for turn in range(len(INPUT), 30_000_000):
    number = turn - haystack[needle] if needle in haystack else 0
    haystack[needle] = turn
    needle = number

print(number)

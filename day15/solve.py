from itertools import count

INPUT = [12, 20, 0, 6, 1, 17, 7]

haystack = dict(zip(INPUT[:-1], count(1)))
needle   = INPUT[-1]

turn = len(INPUT)

while True:
    try:
        index = haystack[needle]
    except KeyError:
        number = 0
    else:
        number = turn - index
    haystack[needle] = turn
    turn += 1
    if turn == 2020: # I know it's inefficient to check this ~30,000,000 times
        print(number)
    elif turn == 30_000_000:
        print(number)
        break
    needle = number

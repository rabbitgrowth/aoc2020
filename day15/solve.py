INPUT = [12, 20, 0, 6, 1, 17, 7]

haystack = {number: index for index, number in enumerate(INPUT[:-1])}
needle   = INPUT[-1]

turn = len(haystack)

while True:
    try:
        index = haystack[needle]
    except KeyError:
        number = 0
    else:
        number = turn - index
    haystack[needle] = turn
    turn += 1
    if turn == 2020 - 1: # I know it's inefficient to check this ~30,000,000 times
        print(number)
    elif turn == 30_000_000 - 1:
        print(number)
        break
    needle = number

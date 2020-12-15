from itertools import count

numbers = [12, 20, 0, 6, 1, 17, 7]

for _ in range(2020 - len(numbers)):
    init, last = numbers[:-1], numbers[-1]
    try:
        index = next(index
                     for index, number in zip(count(len(init) - 1, -1), reversed(init))
                     if number == last)
    except StopIteration:
        number = 0
    else:
        number = len(init) - index
    numbers.append(number)

print(numbers[-1])

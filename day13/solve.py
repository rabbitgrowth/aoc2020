from itertools import count

with open('input.txt') as f:
    start = int(next(f))
    buses = [int(bus) for bus in next(f).split(',') if bus != 'x']

found = False
for timestamp in count(start):
    for bus in buses:
        if timestamp % bus == 0:
            wait = timestamp - start
            print(wait * bus)
            found = True
            break
    if found:
        break

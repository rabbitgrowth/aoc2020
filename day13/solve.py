from collections import namedtuple
from itertools   import count

Bus = namedtuple('Bus', 'id offset')

with open('input.txt') as f:
    start = int(next(f))
    buses = [Bus(int(bus), offset)
             for offset, bus in enumerate(next(f).split(','))
             if bus != 'x']

found = False
for timestamp in count(start):
    for bus in buses:
        if timestamp % bus.id == 0:
            wait = timestamp - start
            print(wait * bus.id)
            found = True
            break
    if found:
        break

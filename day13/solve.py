import math
from collections import namedtuple
from itertools   import count

Bus = namedtuple('Bus', 'id offset')

with open('input.txt') as f:
    start = int(next(f))
    buses = [Bus(int(bus), offset)
             for offset, bus in enumerate(next(f).split(','))
             if bus != 'x']

found = False
for wait, timestamp in enumerate(count(start)):
    for bus in buses:
        if timestamp % bus.id == 0:
            print(wait * bus.id)
            found = True
            break
    if found:
        break

time = 0
step = 1
for bus1, bus2 in zip(buses, buses[1:]):
    step = math.lcm(step, bus1.id)
    for time in count(time, step):
        if (time + bus2.offset) % bus2.id == 0:
            break
print(time)

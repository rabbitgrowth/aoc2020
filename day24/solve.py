import re

DIRECTION = re.compile(r'[sn]?[ew]')

DELTAS = {'e' : ( 1,  0),
          'se': ( 0,  1),
          'sw': (-1,  1),
          'w' : (-1,  0),
          'nw': ( 0, -1),
          'ne': ( 1, -1)}

with open('input.txt') as f:
    tiles = list(map(DIRECTION.findall, f))

black = set()

for tile in tiles:
    point = (0, 0)
    for direction in tile:
        point = tuple(value + delta
                      for value, delta in zip(point, DELTAS[direction]))
    if point in black:
        black.remove(point)
    else:
        black.add(point)

print(len(black))

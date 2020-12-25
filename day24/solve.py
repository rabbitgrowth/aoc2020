import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

DIRECTION = re.compile(r'[sn]?[ew]')

DELTAS = {'e' : Point( 1,  0),
          'se': Point( 0,  1),
          'sw': Point(-1,  1),
          'w' : Point(-1,  0),
          'nw': Point( 0, -1),
          'ne': Point( 1, -1)}

def circumambulate(point):
    for delta in DELTAS.values():
        yield point + delta

with open('input.txt') as f:
    tiles = list(map(DIRECTION.findall, f))

black = set()

for tile in tiles:
    point = Point(0, 0)
    for direction in tile:
        point += DELTAS[direction]
    if point in black:
        black.remove(point)
    else:
        black.add(point)

print(len(black))

for _ in range(100):
    new_black = set()
    changeable = {neighbour
                  for tile in black
                  for neighbour in circumambulate(tile)}
    for tile in changeable:
        black_neighbours = sum(neighbour in black
                               for neighbour in circumambulate(tile))
        if (
            tile in     black and black_neighbours in {1, 2} or # not 0 or >2
            tile not in black and black_neighbours == 2
        ):
            new_black.add(tile)
    black = new_black

print(len(black))

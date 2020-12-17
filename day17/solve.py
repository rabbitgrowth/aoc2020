from collections import namedtuple

Cube = namedtuple('Cube', 'x y z')

def circumambulate(cube):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                if not (dx == 0 and dy == 0 and dz == 0):
                    yield Cube(cube.x + dx, cube.y + dy, cube.z + dz)

with open('input.txt') as f:
    active = {Cube(x, y, 0) # let z = 0
              for y, line in enumerate(f)
              for x, char in enumerate(line.rstrip('\n'))
              if char == '#'}

for _ in range(6):
    new_active = set()
    changeable = {neighbour
                  for cube in active
                  for neighbour in circumambulate(cube)}
    for cube in changeable:
        active_neighbours = sum(neighbour in active
                                for neighbour in circumambulate(cube))
        if (
            cube     in active and active_neighbours in {2, 3} or
            cube not in active and active_neighbours == 3
        ):
            new_active.add(cube)
    active = new_active

print(len(active))

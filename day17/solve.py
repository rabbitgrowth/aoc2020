from itertools import product

def circumambulate(cube): # or hypercube
    for deltas in product((-1, 0, 1), repeat=len(cube)):
        if not all(delta == 0 for delta in deltas): # exclude cube itself
            yield tuple(dimension + delta
                        for dimension, delta in zip(cube, deltas))

for dimensions in (3, 4):
    active = set()

    with open('input.txt') as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.rstrip('\n')):
                if char == '#':
                    active.add((x, y, *[0]*(dimensions-2)))

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

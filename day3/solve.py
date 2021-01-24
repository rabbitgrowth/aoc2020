import math

with open('input.txt') as f:
    MAP = f.read().splitlines()

WIDTH = len(MAP[0])

def count_trees(dx, dy):
    trees = 0
    x, y = 0, 0
    while True:
        x += dx
        y += dy
        try:
            if MAP[y][x % WIDTH] == '#':
                trees += 1
        except IndexError:
            break
    return trees

print(count_trees(3, 1))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(math.prod(count_trees(dx, dy) for dx, dy in slopes))

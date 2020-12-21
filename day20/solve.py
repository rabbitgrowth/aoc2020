import math
from collections import Counter
from functools   import reduce
from operator    import mul

def top   (tile): return tile[ 0]
def bottom(tile): return tile[-1]
def left  (tile): return tuple(row[ 0] for row in tile)
def right (tile): return tuple(row[-1] for row in tile)

def edges(tile):
    for func in (top, bottom, left, right):
        yield func(tile)

def normalize(edge):
    return min(edge, edge[::-1])

def transform(tile):
    for _ in range(4):
        yield tile
        tile = tuple(row[::-1] for row in tile)
        yield tile
        tile = tuple(zip(*tile))

tiles = {}
with open('input.txt') as f:
    pars = f.read().split('\n\n')
    for par in pars:
        lines   = par.splitlines()
        tile_id = int(lines[0].removeprefix('Tile ').removesuffix(':'))
        tile    = tuple(tuple(line) for line in lines[1:])
        tiles[tile_id] = tile

width = int(math.sqrt(len(tiles)))

all_edges = Counter(normalize(edge)
                    for tile in tiles.values()
                    for edge in edges(tile))
corners = [tile_id
           for tile_id, tile in tiles.items()
           if sum(all_edges[normalize(edge)] == 1
                  for edge in edges(tile)) == 2]
print(reduce(mul, corners))

top_left = tiles.pop(corners[0])
for top_left in transform(top_left):
    if all(all_edges[normalize(func(top_left))] == 2
           for func in (right, bottom)):
        break

# [[X]]
puzzle = [[top_left]]

# [[X],
#  [X],
#  [X]]
for _ in range(width - 1):
    found = False
    for tile_id, tile in tiles.items():
        for form in transform(tile):
            if top(form) == bottom(puzzle[-1][0]):
                puzzle.append([form])
                found = True
                break
        if found:
            break
    tiles.pop(tile_id)

# [[X,X,X],
#  [X,X,X],
#  [X,X,X]]
for row in puzzle:
    for _ in range(width - 1):
        found = False
        for tile_id, tile in tiles.items():
            for form in transform(tile):
                if left(form) == right(row[-1]):
                    row.append(form)
                    found = True
                    break
            if found:
                break
        tiles.pop(tile_id)

def remove_border(tile):
    return tuple(row[1:-1] for row in tile[1:-1])

def merge(puzzle):
    return tuple(tuple(pixel for subrow in subrows for pixel in subrow)
                 for row in puzzle
                 for subrows in zip(*row))

sea = merge([[remove_border(tile) for tile in row] for row in puzzle])

monster = ('                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ')

def scan(sea, monster):
    swidth  = len(sea[0])
    sheight = len(sea)
    mwidth  = len(monster[0])
    mheight = len(monster)
    for x in range(swidth - mwidth + 1):
        for y in range(sheight - mheight + 1):
            yield tuple(row[x : x + mwidth]
                        for row in sea[y : y + mheight])

def contains_monster(sea, monster):
    for srow, mrow in zip(sea, monster):
        for spixel, mpixel in zip(srow, mrow):
            if spixel == '.' and mpixel == '#':
                return False
    return True

for form in transform(sea):
    monsters = sum(contains_monster(area, monster)
                   for area in scan(form, monster))
    if monsters != 0:
        spixels = sum(row.count('#') for row in sea)
        mpixels = sum(row.count('#') for row in monster)
        print(spixels - mpixels * monsters)

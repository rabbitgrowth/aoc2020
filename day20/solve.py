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

tiles = {}
with open('input.txt') as f:
    pars = f.read().split('\n\n')
    for par in pars:
        lines   = par.splitlines()
        tile_id = int(lines[0].removeprefix('Tile ').removesuffix(':'))
        tile    = tuple(tuple(line) for line in lines[1:])
        tiles[tile_id] = tile

all_edges = Counter(normalize(edge)
                    for tile in tiles.values()
                    for edge in edges(tile))
corners = [tile_id
           for tile_id, tile in tiles.items()
           if sum(all_edges[normalize(edge)] == 1
                  for edge in edges(tile)) == 2]
print(reduce(mul, corners))

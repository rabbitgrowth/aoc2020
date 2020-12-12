DIRECTIONS = {'E': ( 1,  0),
              'S': ( 0,  1),
              'W': (-1,  0),
              'N': ( 0, -1)}

def clockwise    (dx, dy): return -dy,  dx
def anticlockwise(dx, dy): return  dy, -dx

with open('input.txt') as f:
    moves = []
    for line in f:
        op, num = line[0], line[1:]
        num = int(num)
        moves.append((op, num))

x1, y1 = 0, 0
x2, y2 = 0, 0
reldx, reldy = DIRECTIONS['E'] # Part 1: ship starts by facing east
waydx, waydy = 10, -1          # Part 2: waypoint starts at 10E 1N

for op, num in moves:
    if op in 'LR':
        assert num % 90 == 0
        steps = num // 90
        rotate = clockwise if op == 'R' else anticlockwise
        for _ in range(steps):
            reldx, reldy = rotate(reldx, reldy)
            waydx, waydy = rotate(waydx, waydy)
    elif op == 'F':
        x1 += reldx * num
        y1 += reldy * num
        x2 += waydx * num
        y2 += waydy * num
    elif op in 'ESWN':
        absdx, absdy = DIRECTIONS[op]
        x1    += absdx * num
        y1    += absdy * num
        waydx += absdx * num
        waydy += absdy * num
    else:
        raise ValueError(f'Invalid operation {op}')

print(abs(x1) + abs(y1))
print(abs(x2) + abs(y2))

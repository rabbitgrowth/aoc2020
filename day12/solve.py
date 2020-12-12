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

x, y = 0, 0
reldx, reldy = DIRECTIONS['E']

for op, num in moves:
    if op in 'LR':
        assert num % 90 == 0
        steps = num // 90
        rotate = clockwise if op == 'R' else anticlockwise
        for _ in range(steps):
            reldx, reldy = rotate(reldx, reldy)
    elif op == 'F':
        x += reldx * num
        y += reldy * num
    elif op in 'ESWN':
        absdx, absdy = DIRECTIONS[op]
        x += absdx * num
        y += absdy * num
    else:
        raise ValueError(f'Invalid operation {op}')

print(abs(x) + abs(y))

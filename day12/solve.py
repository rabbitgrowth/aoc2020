DIRS = ['E', 'S', 'W', 'N']

DXDY = {'E': ( 1,  0),
        'S': ( 0,  1),
        'W': (-1,  0),
        'N': ( 0, -1)}

with open('input.txt') as f:
    moves = []
    for line in f:
        op, num = line[0], line[1:]
        num = int(num)
        moves.append((op, num))

x = 0
y = 0
index = 0 # direction index

for op, num in moves:
    if op in 'RL':
        assert num % 90 == 0
        steps = num // 90
        index += steps * (1 if op == 'R' else -1)
    elif op in 'FESWN':
        dx, dy = DXDY[DIRS[index % 4] if op == 'F' else op]
        x += dx * num
        y += dy * num
    else:
        raise ValueError(f'Invalid operation {op}')

print(abs(x) + abs(y))

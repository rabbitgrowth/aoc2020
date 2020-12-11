from copy import deepcopy

with open('input.txt') as f:
    board = [list(line.strip()) for line in f]

def advance(board):
    new_board = deepcopy(board)
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell in 'L#': # floor (.) never changes
                neighbours = []
                for neighbour in circumambulate(x, y):
                    xx, yy = neighbour
                    if xx >= 0 and yy >= 0:
                        try:
                            neighbours.append(board[yy][xx])
                        except IndexError:
                            pass
                if cell == 'L' and neighbours.count('#') == 0:
                    new_board[y][x] = '#'
                elif cell == '#' and neighbours.count('#') >= 4:
                    new_board[y][x] = 'L'
    return new_board

def circumambulate(x, y):
    yield x - 1, y - 1
    yield x,     y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x,     y + 1
    yield x + 1, y + 1

while True:
    new_board = advance(board)
    if new_board == board: # stabilized
        print(sum(cell == '#' for row in board for cell in row))
        break
    board = new_board

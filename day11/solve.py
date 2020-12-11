from copy import deepcopy
from itertools import count

class Board:
    dxdy = [(-1, -1),
            ( 0, -1),
            ( 1, -1),
            (-1,  0),
            ( 1,  0),
            (-1,  1),
            ( 0,  1),
            ( 1,  1)]

    def __init__(self, string):
        self.board = [list(line) for line in string.splitlines()]

    def __iter__(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                yield x, y, cell

    def __eq__(self, other):
        if not isinstance(other, Board):
            return NotImplemented
        return self.board == other.board

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.board)

    def get(self, x, y):
        if x < 0 or y < 0:
            return None
        try:
            return self.board[y][x]
        except IndexError:
            return None

    def set(self, x, y, cell):
        if x < 0 or y < 0:
            raise ValueError('Negative indices not supported')
        try:
            self.board[y][x] = cell
        except IndexError:
            raise ValueError('Coordinates out of bound')

    def advance(self, part):
        if part == 1:
            threshold = 4
        elif part == 2:
            threshold = 5
        else:
            raise ValueError('Part must be 1 or 2')
        new_board = deepcopy(self)
        for x, y, cell in self:
            if cell in 'L#':
                occupied = self.neighbours(x, y, part).count('#')
                if cell == 'L' and occupied == 0:
                    new_board.set(x, y, '#')
                elif cell == '#' and occupied >= threshold:
                    new_board.set(x, y, 'L')
        return new_board

    def neighbours(self, x, y, part):
        cells = []
        if part == 1:
            for dx, dy in self.dxdy:
                cell = self.get(x + dx, y + dy)
                if cell is not None:
                    cells.append(cell)
        elif part == 2:
            for dx, dy in self.dxdy:
                for i in count(1):
                    cell = self.get(x + i*dx, y + i*dy)
                    if cell is None:
                        break
                    elif cell in 'L#':
                        cells.append(cell)
                        break
        else:
            raise ValueError('Part must be 1 or 2')
        return cells

    def count(self, cell):
        return sum(row.count(cell) for row in self.board)

with open('input.txt') as f:
    string = f.read()
    for part in [1, 2]:
        board = Board(string)
        while True:
            new_board = board.advance(part)
            if new_board == board: # stabilized
                print(new_board.count('#'))
                break
            board = new_board

from copy import deepcopy

class Board:
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

    def advance(self):
        new_board = deepcopy(self)
        for x, y, cell in self:
            if cell in 'L#':
                occupied = self.neighbours(x, y).count('#')
                if cell == 'L' and occupied == 0:
                    new_board.set(x, y, '#')
                elif cell == '#' and occupied >= 4:
                    new_board.set(x, y, 'L')
        return new_board

    def neighbours(self, x, y):
        cells = []
        for x, y in [(x - 1, y - 1),
                     (x,     y - 1),
                     (x + 1, y - 1),
                     (x - 1, y    ),
                     (x + 1, y    ),
                     (x - 1, y + 1),
                     (x,     y + 1),
                     (x + 1, y + 1)]:
            cell = self.get(x, y)
            if cell is not None:
                cells.append(cell)
        return cells

    def count(self, cell):
        return sum(row.count(cell) for row in self.board)

with open('input.txt') as f:
    board = Board(f.read())
    while True:
        new_board = board.advance()
        if new_board == board: # stabilized
            print(new_board.count('#'))
            break
        board = new_board

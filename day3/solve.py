with open('input.txt') as f:
    GEOLOGY = f.read().splitlines()

WIDTH = len(GEOLOGY[0])

def count_trees(dx, dy):
    x, y = 0, 0
    trees = 0
    while True:
        x += dx
        y += dy
        try:
            if GEOLOGY[y][x % WIDTH] == '#':
                trees += 1
        except IndexError:
            break
    return trees

if __name__ == '__main__':
    answer1 = count_trees(3, 1)
    answer2 = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        answer2 *= count_trees(dx, dy)
    print(answer1)
    print(answer2)

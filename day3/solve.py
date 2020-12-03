with open('input.txt') as f:
    MAP = f.read().splitlines()

WIDTH = len(MAP[0])

def count_trees(slope):
    x, y = 0, 0
    dx, dy = slope
    trees = 0
    while True:
        x += dx
        y += dy
        try:
            if MAP[y][x % WIDTH] == '#':
                trees += 1
        except IndexError:
            break
    return trees

if __name__ == '__main__':
    answer1 = count_trees((3, 1))
    answer2 = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        answer2 *= count_trees(slope)
    print(answer1)
    print(answer2)

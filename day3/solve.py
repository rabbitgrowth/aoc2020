with open('input.txt') as f:
    geology = f.read().splitlines()

width = len(geology[0])

x, y = 0, 0

trees = 0
while True:
    x += 3
    y += 1
    try:
        if geology[y][x % width] == '#':
            trees += 1
    except IndexError:
        break
print(trees)

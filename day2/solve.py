import re

PATTERN = re.compile(r'(\d+)-(\d+) (.): (.+)')

def parse(line):
    x, y, letter, password = PATTERN.match(line).groups()
    x = int(x)
    y = int(y)
    return x, y, letter, password

if __name__ == '__main__':
    count1 = 0
    count2 = 0
    with open('input.txt') as f:
        for line in f:
            x, y, letter, password = parse(line)
            if x <= password.count(letter) <= y:
                count1 += 1
            if sum([password[x - 1] == letter,
                    password[y - 1] == letter]) == 1:
                count2 += 1
    print(count1)
    print(count2)

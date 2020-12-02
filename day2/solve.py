import re

PATTERN = re.compile(r'(\d+)-(\d+) (.): (.+)')

def parse(line):
    minimum, maximum, letter, password = PATTERN.match(line).groups()
    minimum = int(minimum)
    maximum = int(maximum)
    return minimum, maximum, letter, password

if __name__ == '__main__':
    count = 0
    with open('input.txt') as f:
        for line in f:
            minimum, maximum, letter, password = parse(line)
            if minimum <= password.count(letter) <= maximum:
                count += 1
    print(count)

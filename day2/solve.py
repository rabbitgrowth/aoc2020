import re

PATTERN = re.compile(r'(\d+)-(\d+) (.): (.+)')

count1 = 0
count2 = 0

with open('input.txt') as f:
    for line in f:
        x, y, letter, password = PATTERN.match(line).groups()
        x = int(x)
        y = int(y)
        if x <= password.count(letter) <= y:
            count1 += 1
        if sum(password[index - 1] == letter for index in [x, y]) == 1:
            count2 += 1

print(count1)
print(count2)

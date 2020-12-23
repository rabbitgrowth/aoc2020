from copy     import copy
from operator import mul

def follow(links, cup, n):
    for _ in range(n):
        yield (cup := links[cup])

def link(cups):
    return {a: b for a, b in zip(cups, [*cups[1:], cups[0]])}

with open('input.txt') as f:
    cups1 = list(map(int, f.read().strip()))
    cups2 = copy(cups1)
    cups2.extend(range(len(cups1) + 1, 1_000_000 + 1))

links1 = link(cups1)
links2 = link(cups2)

def show1(links):
    print(''.join(map(str, follow(links, 1, len(links) - 1))))

def show2(links):
    print(mul(*follow(links, 1, 2)))

for links, times, show in ((links1, 100,        show1),
                           (links2, 10_000_000, show2)):
    current = cups1[0]

    for _ in range(times):
        picks = list(follow(links, current, 3))
        links[current] = links[picks[-1]]

        dest = current - 1
        while True:
            if dest not in picks and dest in links:
                break
            if dest < 1:
                dest = len(links)
                continue
            dest -= 1

        links[picks[-1]] = links[dest]
        links[dest]      = picks[0]

        current = links[current]

    show(links)

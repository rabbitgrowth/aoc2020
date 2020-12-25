from itertools import count

DIVISOR = 20201227

def get_loop_size(public_key):
    value = 1
    for loop_size in count(1):
        value *= 7
        value %= DIVISOR
        if value == public_key:
            return loop_size

with open('input.txt') as f:
    card_public_key = int(next(f))
    door_public_key = int(next(f))

card_loop_size = get_loop_size(card_public_key)

value = 1
for _ in range(card_loop_size):
    value *= door_public_key
    value %= DIVISOR
print(value) # encryption key

TABLE = str.maketrans('FBLR', '0101')

with open('input.txt') as f:
    seats = {int(seat.translate(TABLE), 2) for seat in f}

print(max(seats))
for seat in seats:
    if seat + 1 not in seats:
        print(seat + 1)
        break

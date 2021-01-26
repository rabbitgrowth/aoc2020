TABLE = str.maketrans('FBLR', '0101')

def seat_id(seat):
    return int(seat.translate(TABLE), 2)

with open('input.txt') as f:
    seat_ids = set(map(seat_id, f))

print(max(seat_ids))
for seat_id in seat_ids:
    if seat_id + 1 not in seat_ids:
        print(seat_id + 1)
        break

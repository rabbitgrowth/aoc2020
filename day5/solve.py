def search(chars):
    lo = 0
    hi = 2 ** len(chars)
    diff = hi
    for char in chars:
        diff //= 2
        if char in 'FL':
            hi -= diff
        elif char in 'BR':
            lo += diff
        else:
            raise AssertionError(f'Invalid character {char}')
    assert diff    == 1
    assert hi - lo == 1
    return lo

def seat_id(seat):
    row, column = seat[:7], seat[7:]
    return search(row) * 8 + search(column)

if __name__ == '__main__':
    with open('input.txt') as f:
        seat_ids = {seat_id(line.strip()) for line in f}
        print(max(seat_ids))
        for seat_id in sorted(seat_ids):
            if seat_id + 1 not in seat_ids:
                print(seat_id + 1)
                break

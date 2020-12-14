memory = {}

with open('input.txt') as f:
    for line in f:
        lhs, rhs = line.strip().split(' = ')
        if lhs == 'mask':
            mask = rhs
        else:
            index  = int(lhs.removeprefix('mem[').removesuffix(']'))
            padded = bin(int(rhs)).removeprefix('0b').rjust(36, '0')
            memory[index] = ''.join(old if new == 'X' else new
                                    for old, new in zip(padded, mask))

print(sum(int(value, base=2) for value in memory.values()))

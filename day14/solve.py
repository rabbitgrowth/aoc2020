from itertools import product

def pad(integer):
    # 12 (decimal) -> '000000000000000000000000000000001100' (binary)
    return bin(integer).removeprefix('0b').rjust(36, '0')

memory1 = {}
memory2 = {}

with open('input.txt') as f:
    for line in f:
        lhs, rhs = line.strip().split(' = ')
        if lhs == 'mask':
            mask = rhs
        else:
            # mem[index] = value
            #     ^^^^^    ^^^^^ ints
            index = int(lhs.removeprefix('mem[').removesuffix(']'))
            value = int(rhs)
            # Part 1
            masked = ''.join(old if new == 'X' else new
                             for old, new in zip(pad(value), mask))
            memory1[index] = int(masked, base=2)
            # Part 2
            floating  = []
            x_indices = []
            for index, (old, new) in enumerate(zip(pad(index), mask)):
                if new == '0':
                    floating.append(old)
                elif new == '1':
                    floating.append('1')
                elif new == 'X':
                    floating.append(None) # filler
                    x_indices.append(index)
                else:
                    raise ValueError(f'Invalid character {new}')
            for choices in product('01', repeat=len(x_indices)):
                for x_index, choice in zip(x_indices, choices):
                    floating[x_index] = choice
                index = int(''.join(floating), base=2) # convert to decimal just to be neat
                memory2[index] = value

print(sum(memory1.values()))
print(sum(memory2.values()))

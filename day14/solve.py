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
            masked = ''.join(v if m == 'X' else m
                             for v, m in zip(pad(value), mask))
            memory1[index] = int(masked, base=2)
            # Part 2
            masked = []
            for i, m in zip(pad(index), mask):
                if m == '0':
                    masked.append(i)
                elif m == '1':
                    masked.append('1')
                elif m == 'X':
                    masked.append('01')
            for combination in product(*masked):
                index = int(''.join(combination), base=2) # convert to decimal just to be neat
                memory2[index] = value

print(sum(memory1.values()))
print(sum(memory2.values()))

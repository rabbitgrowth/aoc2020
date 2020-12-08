with open('input.txt') as f:
    program = []
    for line in f:
        operation, argument = line.split()
        argument = int(argument)
        program.append((operation, argument))

pointer     = 0
accumulator = 0

seen = set()

while pointer not in seen:
    seen.add(pointer)
    operation, argument = program[pointer]
    if operation == 'acc':
        accumulator += argument
        pointer += 1
    elif operation == 'jmp':
        pointer += argument
    elif operation == 'nop':
        pointer += 1

print(accumulator)

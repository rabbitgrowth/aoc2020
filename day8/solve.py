from copy import copy

def run(program):
    pointer     = 0
    accumulator = 0
    seen = set()
    while True:
        seen.add(pointer)
        operation, argument = program[pointer]
        if operation == 'acc':
            accumulator += argument
            pointer += 1
        elif operation == 'jmp':
            pointer += argument
        elif operation == 'nop':
            pointer += 1
        if pointer in seen:
            return accumulator, 1 # "infinite loop detected"
        if pointer == len(program):
            return accumulator, 0 # "program terminated normally"

with open('input.txt') as f:
    program = []
    for line in f:
        operation, argument = line.split()
        argument = int(argument)
        program.append((operation, argument))

accumulator, exit_status = run(program)
assert exit_status == 1
print(accumulator)

for i, (operation, argument) in enumerate(program):
    program_copy = copy(program)
    if operation == 'jmp':
        program_copy[i] = ('nop', argument)
    elif operation == 'nop':
        program_copy[i] = ('jmp', argument)
    else:
        continue
    accumulator, exit_status = run(program_copy)
    if exit_status == 0:
        print(accumulator)

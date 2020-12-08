from copy import copy

def parse(file):
    program = []
    with open(file) as f:
        for line in f:
            operation, argument = line.split()
            argument = int(argument)
            program.append((operation, argument))
    return program

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

if __name__ == '__main__':
    program = parse('input.txt')

    # Part 1
    accumulator, exit_status = run(program)
    assert exit_status == 1
    print(accumulator)

    # Part 2
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

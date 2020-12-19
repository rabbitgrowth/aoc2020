import re

def parse(paragraph):
    grammar = {}
    for line in paragraph.splitlines():
        lhs, rhs = line.split(': ')
        rule = int(lhs)
        if '|' in rhs:   # e.g., 2 3 | 3 2
            expansion = [tuple(map(int, choice.split()))
                         for choice in rhs.split(' | ')]
        elif '"' in rhs: # e.g., "a"
            expansion = tuple(rhs.removeprefix('"').removesuffix('"'))
        else:            # e.g., 4 1 5
            expansion = tuple(map(int, rhs.split()))
        grammar[rule] = expansion
    return grammar

def expand(tokens, grammar):
    result = ''
    for token in tokens:
        if token not in grammar: # cannot be expanded further
            result += token
        else:
            expansion = grammar.get(token)
            if isinstance(expansion, list):
                choices = '|'.join(expand(choice, grammar)
                                   for choice in expansion)
                result += f'(?:{choices})'
            else:
                result += expand(expansion, grammar)
    return result

with open('input.txt') as f:
    par1, par2 = f.read().split('\n\n')
    grammar  = parse(par1)
    regex    = re.compile('^' + expand((0,), grammar) + '$')
    messages = par2.splitlines()
    print(sum(regex.search(message) is not None
              for message in messages))

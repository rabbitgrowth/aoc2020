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
    grammar    = parse(par1)
    messages   = par2.splitlines()
    zero       = expand(( 0,), grammar)
    forty_two  = expand((42,), grammar)
    thirty_one = expand((31,), grammar)
    regex1     = re.compile(f'^{zero}$')
    regex2     = re.compile(f'^(({forty_two})+)(({thirty_one})+)$')
    count1     = 0
    count2     = 0
    for message in messages:
        if regex1.search(message):
            count1 += 1
        match2 = regex2.search(message)
        if match2:
            forty_twos  = len(match2.group(1)) // len(match2.group(2))
            thirty_ones = len(match2.group(3)) // len(match2.group(4))
            if forty_twos > thirty_ones:
                count2 += 1
    print(count1)
    print(count2)

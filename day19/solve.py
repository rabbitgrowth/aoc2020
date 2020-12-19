# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

rules = {
    0: (4, 1, 5),
    1: [(2, 3), (3, 2)],
    2: [(4, 4), (5, 5)],
    3: [(4, 5), (5, 4)],
    4: ('a',),
    5: ('b',),
}

def expand(tokens):
    result = ''
    for token in tokens:
        if token not in rules: # cannot be expanded further
            result += token
        else:
            expansion = rules.get(token)
            if isinstance(expansion, list):
                choices = '|'.join(map(expand, expansion))
                result += f'({choices})'
            else:
                result += expand(expansion)
    return result

print(expand((0,)))

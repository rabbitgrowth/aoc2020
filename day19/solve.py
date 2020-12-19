rules = {
    0: [1, 2],
    1: ['a'],
    2: [1, 3],
    3: ['b'],
}

def expand(tokens):
    result = []
    for token in tokens:
        if token not in rules: # cannot be expanded further
            result.append(token)
        else:
            result.extend(expand(rules[token]))
    return result

print(expand([0]))

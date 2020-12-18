import re
from operator import add, mul

WORD = re.compile(r'\d+|[+*()]')
FUNCTIONS = {'+': add, '*': mul}

def tokenize(expression):
    for word in WORD.findall(expression):
        if word in FUNCTIONS:
            yield FUNCTIONS[word]
        elif word in '()':
            yield word
        else:
            yield int(word)

def group(tokens):
    groups = []
    for token in tokens:
        if token == '(':
            groups.append([])
        elif token == ')':
            result = evaluate(groups.pop())
            if not groups:
                return result
            groups[-1].append(result)
        else:
            groups[-1].append(token)

def evaluate(tokens):
    if len(tokens) == 1:
        return tokens[0]
    x, function, y = tokens[:3]
    result = function(x, y)
    return evaluate([result, *tokens[3:]])

def calculate(expression):
    tokens = tokenize(expression)
    return group(tokens)

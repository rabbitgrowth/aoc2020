from itertools import chain
from operator  import add, mul

FUNCTIONS = {'+': add, '*': mul}

def tokenize(expression):
    for word in expression.split():
        yield FUNCTIONS[word] if word in FUNCTIONS else int(word)

def evaluate(tokens):
    x = next(tokens)
    try:
        function, y = next(tokens), next(tokens)
    except StopIteration:
        return x
    result = function(x, y)
    return evaluate(chain((result,), tokens))

def calculate(expression):
    tokens = tokenize(expression)
    return evaluate(tokens)

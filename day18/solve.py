import re
from collections import deque, namedtuple
from operator    import add, mul

WORD = re.compile(r'\d+|[+*()]')
FUNCTIONS = {'+': add, '*': mul}

Function = namedtuple('Function', 'function precedence')

def tokenize(expression):
    precedence = 0
    for word in WORD.findall(expression):
        if word in FUNCTIONS:
            yield Function(FUNCTIONS[word], precedence)
        elif word == '(':
            precedence += 1
        elif word == ')':
            precedence -= 1
        else:
            yield int(word)

def evaluate(tokens):
    queue = deque(tokens)
    stack = [queue.popleft()]
    while queue:
        stack.extend(queue.popleft() for _ in range(2))
        peek = queue[0] if queue else None
        reduce(stack, peek)
    (result,) = stack
    return result

def reduce(stack, peek):
    while len(stack) > 1:
        function = stack[-2]
        if peek is None or function.precedence >= peek.precedence:
            y, _, x = (stack.pop() for _ in range(3))
            reduction = function.function(x, y)
            stack.append(reduction)
        else:
            break

def calculate(expression):
    tokens = tokenize(expression)
    return evaluate(tokens)

with open('input.txt') as f:
    print(sum(map(calculate, f)))

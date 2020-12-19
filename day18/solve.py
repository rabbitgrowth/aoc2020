import re
from collections import deque, namedtuple
from operator    import add, mul

WORD = re.compile(r'\d+|[+*()]')

Function = namedtuple('Function', 'function precedence')

def tokenize(expression, add_precedence=False):
    level = 0
    for word in WORD.findall(expression):
        if word == '+':
            yield Function(add, level + add_precedence)
        elif word == '*':
            yield Function(mul, level)
        elif word == '(':
            level += 2
        elif word == ')':
            level -= 2
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

def calculate(expression, add_precedence=False):
    tokens = tokenize(expression, add_precedence=add_precedence)
    return evaluate(tokens)

with open('input.txt') as f:
    lines = list(f)
    print(sum(calculate(line)                      for line in lines))
    print(sum(calculate(line, add_precedence=True) for line in lines))

OPERANDS = {'+': lambda x, y : x + y,
            '-': lambda x, y : x - y,
            '*': lambda x, y : x * y,
            '/': lambda x, y : x / y}

def rpn_calculator(inputs):
    stack = []
    for inp in inputs:
        if inp in OPERANDS:
            second = stack.pop()
            first = stack.pop()
            stack.append(OPERANDS[inp](first, second))
        else:
            stack.append(float(inp))
    return stack.pop()

inputs = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
expected = 5
assert rpn_calculator(inputs) == expected

inputs = [99, 11, '/', 1, '+']
expected = 10
assert rpn_calculator(inputs) == expected
import operator

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}


def postfix_eval(expr):
    stack = []
    for elem in expr.split():
        if elem in operators:
            assert len(stack) >= 2, "Not enough arguments"
            right, left = stack.pop(), stack.pop()
            if elem == '/':
                assert right != 0, "Division by zero."
            stack.append(operators[elem](left, right))
        else:
            stack.append(int(elem))
    assert len(stack) == 1, "Not enough operators"
    return stack[0]


print(postfix_eval("1 3 4 * + 2 -"))
print(postfix_eval("3 2 1 + + 2 /"))
print(postfix_eval("2 +"))

from functools import reduce


def operate(n, *args):

    def addition():
        return reduce(lambda x, y: (x + y), args)

    def multiply():
        return reduce(lambda x, y: x * y, args)

    def subtract():
        return reduce(lambda x, y: x - y, args)

    def division():
        return reduce(lambda x, y: x / y, args)

    if n == '+':
        return addition()
    elif n == '-':
        return subtract()
    elif n == '*':
        return multiply()
    elif n == '/':
        return division()


print(operate('+', 1, 2, 3))
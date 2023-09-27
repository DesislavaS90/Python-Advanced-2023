from functools import reduce

expression = input().split()

index = 0

while index < len(expression):
    element = expression[index]

    if element in '+-*/':
        current_index = expression[:index]
        if element == '*':
            result = reduce((lambda x, y: int(x) * int(y)), current_index)
        elif element == '/':
            result = reduce((lambda x, y: int(x) / int(y)), current_index)
        elif element == '-':
            result = reduce((lambda x, y: int(x) - int(y)), current_index)
        elif element == '+':
            result = reduce((lambda x, y: int(x) + int(y)), current_index)

        [expression.pop(1) for i in range(index)]
        expression[0] = result
        index = 0

    index += 1

print(int(*expression))


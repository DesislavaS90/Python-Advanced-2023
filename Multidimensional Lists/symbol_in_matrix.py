rows = int(input())

matrix = []
result = ()

for r in range(rows):
    matrix.append(list(input()))

symbol = input()

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            result = row, col
            break
        if result:
            break
if result:
    print(result)
else:
    print(f'{symbol} does not occur in the matrix')

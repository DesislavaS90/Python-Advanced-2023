rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for column_index in range(columns):
    result = 0
    for row_index in range(rows):
        result += matrix[row_index][column_index]
    print(result)


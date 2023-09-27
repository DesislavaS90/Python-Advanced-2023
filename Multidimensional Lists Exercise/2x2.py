rows, columns = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
result = 0

for r in range(rows - 1):
    for c in range(columns - 1):
        symbol = matrix[r][c]

        if matrix[r][c + 1] == symbol and matrix[r + 1][c] == symbol and matrix[r + 1][c + 1] == symbol:
            result += 1
print(result)
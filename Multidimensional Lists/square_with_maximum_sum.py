rows, columns = [int(x) for x in input().split(', ')]

matrix = []
result = []
total_sum = 0

for row in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)

for i in range(len(matrix) - 1):
    for k in range(columns - 1):
        first = [matrix[i][k], matrix[i][k+1]]
        second = [matrix[i+1][k], matrix[i+1][k+1]]
        if sum(first) + sum(second) > total_sum:
            result.clear()
            result.append(first)
            result.append(second)
            total_sum = sum(first) + sum(second)

for i in range(len(result)):
    print(*result[i])
print(total_sum)



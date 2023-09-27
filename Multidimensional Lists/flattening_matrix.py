rows = int(input())

matrix = []
flatten_matrix = []

for row in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)

for r in matrix:
    for item in r:
        flatten_matrix.append(item)

print(flatten_matrix)

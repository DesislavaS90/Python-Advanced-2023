rows = int(input())

matrix = []

for row in range(rows):
    columns =[int(x) for x in input().split()]
    matrix.append(columns)

result = 0
for num in range(len(matrix)):
    result += matrix[num][num]
print(result)
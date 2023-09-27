n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary = [matrix[x][x] for x in range(len(matrix))]
secondary = [matrix[x][n - x - 1] for x in range(len(matrix))]

print(abs(sum(primary) - sum(secondary)))


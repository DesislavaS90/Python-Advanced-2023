rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
primary = [matrix[num][num] for num in range(len(matrix))]
secondary = [matrix[num][rows - num - 1] for num in range(len(matrix))]


print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
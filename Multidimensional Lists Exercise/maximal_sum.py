rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
biggest = []

for r in range(rows - 2):
    for c in range(cols - 2):
        first = matrix[r][c:c+3]
        second = matrix[r + 1][c:c+3]
        third = matrix[r + 2][c:c+3]

        current_sum = sum(first) + sum(second) + sum(third)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest = [first, second, third]
print(f'Sum = {max_sum}')
[print(*biggest[row]) for row in range(3)]


n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    row, col, num = int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < n and 0 <= col < n):
        print(f'Invalid coordinates')

    elif command[0] == 'Add':
        matrix[row][col] += num

    elif command[0] == 'Subtract':
        matrix[row][col] -= num

[print(*x) for x in matrix]

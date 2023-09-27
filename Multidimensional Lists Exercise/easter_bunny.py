size = int(input())

matrix = []
bunny_pos = []
best_way = []

best_direction = None
max_collected = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction, positions in directions.items():
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]

    current_way = []
    collected = 0

    while 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == 'X':
            break

        collected += int(matrix[row][col])
        current_way.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected >= max_collected:
        max_collected = collected
        best_direction = direction
        best_way = current_way

print(best_direction)
print(*best_way, sep='\n')
print(max_collected)




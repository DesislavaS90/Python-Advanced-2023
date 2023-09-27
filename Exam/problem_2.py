rows, cols = [int(x) for x in input().split()]

touched_opponents = 0
moves_made = 0
my_position = []

matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    line = input().split()
    matrix.append(line)

    if 'B' in line:
        my_position = [row, line.index('B')]


while True:
    command = input()

    if command == 'Finish':
        break

    if touched_opponents == 3:
        break

    r = directions[command][0] + my_position[0]
    c = directions[command][1] + my_position[1]

    if not 0 <= r < rows or not 0 <= c < cols:
        continue

    if matrix[r][c] == 'O':
        continue

    elif matrix[r][c] == 'P':
        my_position = [r, c]
        matrix[r][c] = '-'
        touched_opponents += 1
        moves_made += 1

    else:
        my_position = [r, c]
        moves_made += 1

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {moves_made}')

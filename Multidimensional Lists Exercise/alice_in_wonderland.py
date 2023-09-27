size = int(input())

matrix = []

alise_pos = []
tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alise_pos = [row, matrix[row].index('A')]
        matrix[row][alise_pos[1]] = '*'

while tea_bags < 10:
    command = input()

    row = alise_pos[0] + directions[command][0]
    col = alise_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alise_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '*'

    if position == 'R':
        break

    if position.isdigit():
        tea_bags += int(position)

if tea_bags >= 10:
    print('She did it! She went to the party.')

else:
    print('Alice didn\'t make it to the tea party.')

[print(*x) for x in matrix]




size = 5

matrix = []

my_position = []
target_count = 0
shoot_targets_count = 0
target_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for x in range(size):
    data = input().split()
    matrix.append(data)

    if 'A' in matrix[x]:
        my_position = [x, matrix[x].index('A')]
        matrix[x][my_position[1]] = '.'

    if 'x' in matrix[x]:
        target_count += data.count('x')

for n in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        direction, step = command[1], int(command[2])
        row = my_position[0] + (directions[direction][0] * step)
        col = my_position[1] + (directions[direction][1] * step)

        if 0 <= row < size and 0 <= col < size:
            if matrix[row][col] != 'x':
                my_position = (row, col)

    elif command[0] == 'shoot':
        direction1 = command[1]
        row = my_position[0] + (directions[direction1][0])
        col = my_position[1] + (directions[direction1][1])

        while 0 <= row < size and 0 <= col < size:
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                target_pos.append([row, col])
                shoot_targets_count += 1
                break

            row += directions[direction1][0]
            col += (directions[direction1][1])

        if target_count == shoot_targets_count:
            print(f'Training completed! All {target_count} targets hit.')
            break

else:
    print(f'Training not completed! {target_count - shoot_targets_count} targets left.')

[print(x, sep='\n') for x in target_pos]




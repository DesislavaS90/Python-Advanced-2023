rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for x in range(rows)]

while True:
    command = input()

    if command == 'END':
        break

    command = command.split()

    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
        continue

    points = list(map(int, command[1:]))

    if points[0] < 0 or points[1] < 0 or points[2] < 0 or points[3] < 0\
            or points[0] >= rows or points[1] >= cols or points[2] >= rows or points[3] >= cols:
        print('Invalid input!')
        continue

    matrix[points[0]][points[1]], matrix[points[2]][points[3]] = \
        matrix[points[2]][points[3]], matrix[points[0]][points[1]]

    [print(*row, sep=' ') for row in matrix]



number_of_presents = int(input())
size = int(input())

matrix = []

santa_pos = []
nice_kids = 0
nice_kid_present = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

for row in range(size):
    data = input().split()
    matrix.append(data)

    if 'S' in matrix[row]:
        santa_pos = [row, matrix[row].index('S')]
        matrix[row][santa_pos[1]] = '-'

    nice_kids += data.count('V')

while True:
    command = input()

    if command == 'Christmas morning':
        break

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]
    visit = matrix[santa_pos[0]][santa_pos[1]]

    if visit == 'V':
        nice_kid_present += 1
        number_of_presents -= 1

    elif visit == 'C':
        for k, v in directions.values():
            row = santa_pos[0] + k
            col = santa_pos[1] + v

            if matrix[row][col].isalpha():
                if matrix[row][col] == 'V':
                    nice_kid_present += 1
                number_of_presents -= 1
                matrix[row][col] = '-'
            if number_of_presents == 0:
                break

    matrix[santa_pos[0]][santa_pos[1]] = '-'

    if number_of_presents == 0 or nice_kids == nice_kid_present:
        break

matrix[santa_pos[0]][santa_pos[1]] = 'S'

if number_of_presents == 0 and nice_kid_present < nice_kids:
    print(f'Santa ran out of presents!')

[print(*x) for x in matrix]

if nice_kid_present == nice_kids:
    print(f'Good job, Santa! {nice_kid_present} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - nice_kid_present} nice kid/s.')


size = int(input())

#matrix = [[0K0K0], [K000K], [00K00], [K000K], [0K0K0]]

matrix = [list(input()) for x in range(size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    the_best_knight = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                k_attacks = 0

                for pos in positions:
                    p1 = row + pos[0]
                    p2 = col + pos[1]

                    if 0 <= p1 < size and 0 <= p2 < size:
                        if matrix[p1][p2] == 'K':
                            k_attacks += 1

                if k_attacks > max_attacks:
                    the_best_knight = [row, col]
                    max_attacks = k_attacks
    if the_best_knight:
        r, c = the_best_knight
        matrix[r][c] = '0'
        removed_knights += 1

    else:
        break
print(removed_knights)
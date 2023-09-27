rows, cols = [int(x) for x in input().split()]

el = ord('a')

for row in range(el, el + rows):
    for col in range(el, el + cols):
        print(f'{chr(row)}{chr(row + col - el)}{chr(row)}', end=' ')
    print()
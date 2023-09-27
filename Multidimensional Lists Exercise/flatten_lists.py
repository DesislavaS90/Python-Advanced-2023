data = input().split('|')

matrix = []

for d in data[::-1]:
    my_d = d.split()
    matrix.extend(my_d)

print(*matrix)
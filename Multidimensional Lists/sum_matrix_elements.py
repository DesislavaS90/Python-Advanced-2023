rows, columns = [int(x) for x in input().split(', ')]

my_matrix = []

for row in range(rows):
    data = [int(x) for x in input().split(', ')]
    my_matrix.append(data)

total_sum = 0
for r in my_matrix:
    total_sum += sum(r)

print(total_sum)
print(my_matrix)


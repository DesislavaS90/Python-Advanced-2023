n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n + 1):
    result = sum(ord(el) for el in input()) // row

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
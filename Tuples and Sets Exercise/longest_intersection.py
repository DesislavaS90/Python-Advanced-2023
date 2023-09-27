n = int(input())

my_set = set()

for _ in range(n):
    first, second = [el.split(',') for el in input().split('-')]

    my_first = set(range(int(first[0]), int(first[1]) + 1))
    my_second = set(range(int(second[0]), int(second[1]) + 1))

    result = my_first.intersection(my_second)

    if len(my_set) < len(result):
        my_set = result

print(f'Longest intersection is [{", ".join(map(str, my_set))}] with length {len(my_set)}')

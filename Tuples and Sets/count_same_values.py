numbers = tuple(map(float, input().split()))

numbers_count = {}

for number in numbers:
    if number not in numbers_count:
        numbers_count[number] = 0
    numbers_count[number] += 1

for n, o in numbers_count.items():
    print(f'{n} - {o} times')
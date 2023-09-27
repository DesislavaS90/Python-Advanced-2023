n = int(input())

data_set = set()

for _ in range(n):
    command, plate = input().split(', ')
    if command == 'IN':
        data_set.add(plate)
    else:
        data_set.remove(plate)


if data_set:
    for plate in data_set:
        print(plate)
else:
    print('Parking Lot is Empty')


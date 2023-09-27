first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

for _ in range(int(input())):
    command, *data = input().split()
    current_command = command + ' ' + data.pop(0)

    if current_command == 'Add First':
        [first.add(int(el)) for el in data]
    elif current_command == 'Add Second':
        [second.add(int(el)) for el in data]
    elif current_command == 'Remove First':
        [first.discard(int(el)) for el in data]
    elif current_command == 'Remove Second':
        [second.discard(int(el)) for el in data]
    else:
        if first.issubset(second) or second.issubset(first):
            print('True')
        else:
            print('False')

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')

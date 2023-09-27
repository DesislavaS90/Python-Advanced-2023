from _collections import deque


def adding_people():
    people = deque()
    while True:
        name = input()
        if name == 'Start':
            break
        people.append(name)
    return people


water = int(input())
names = adding_people()

while True:
    command = input()

    if command == 'End':
        print(f'{water} liters left')
        break
    elif command.startswith('refill'):
        refill_command = command.split(' ')
        refill_water = int(refill_command[1])
        water += refill_water

    else:
        liters = int(command)
        if water >= liters:
            print(f'{names.popleft()} got water')
            water -= liters
        else:
            print(f'{names.popleft()} must wait')




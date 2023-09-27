lines = int(input())

my_stack = []

while lines > 0:
    command = input().split()
    lines -= 1

    if command[0] == '1':
        my_stack.append(int(command[1]))

    elif command[0] == '2':
        if my_stack:
            my_stack.pop()

    elif command[0] == '3' and my_stack:
        if my_stack:
            print(max(my_stack))

    elif command[0] == '4' and my_stack:
        if my_stack:
            print(min(my_stack))

my_stack.reverse()
print(*my_stack, sep=', ')

from collections import deque

kids_names = input().split(' ')
toss = int(input())
my_deque = deque(kids_names)
counter = 0

while len(my_deque) > 1:
    counter += 1
    current_name = my_deque.popleft()

    if counter == toss:
        print(f'Removed {current_name}')
        counter = 0
    else:
        my_deque.append(current_name)
print(f'Last is {my_deque[0]}')
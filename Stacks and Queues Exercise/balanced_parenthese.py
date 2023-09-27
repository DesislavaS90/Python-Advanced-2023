from collections import deque

parentheses = deque(input())

result = deque()

while parentheses:
    my_data = parentheses.popleft()

    if my_data in '({[':
        result.append(my_data)
    elif not result:
        print('NO')
        break
    else:
        if result.pop() + my_data not in '{}[]()':
            print('NO')
            break
else:
    print('YES')

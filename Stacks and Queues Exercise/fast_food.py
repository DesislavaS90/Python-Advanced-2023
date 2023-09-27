from collections import deque

quantity_of_food = int(input())
orders = deque([int(order) for order in input().split()])

print(max(orders))

for _ in range(len(orders)):

    if quantity_of_food >= orders[0]:
        quantity_of_food -= orders[0]
        current_order = orders.popleft()
    else:
        break

if orders:
    print(f"Orders left: {' '.join([str(o) for o in orders])}")
else:
    print('Orders complete')
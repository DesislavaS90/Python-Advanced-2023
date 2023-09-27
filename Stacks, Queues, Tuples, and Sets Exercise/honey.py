from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0

collection = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

while bees and nectar:
    bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar > bee:
        total_honey += abs(collection[symbols.popleft()](bee, current_nectar))
    elif current_nectar < bee:
        bees.appendleft(bee)
print(f'Total honey made: {total_honey}')

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
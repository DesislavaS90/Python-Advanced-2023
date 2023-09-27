from collections import deque

substrings = deque(input().split())

main_colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {
     'orange': {'red', 'yellow'},
     'purple': {'red', 'blue'},
     'green': {'yellow', 'blue'},
}

result = []

while substrings:
    first = substrings.popleft()
    second = substrings.pop() if substrings else ''

    for color in (first + second, second + first):
        if color in main_colors:
            result.append(color)
            break
    else:
        for el in (first[:-1], second[:-1]):
            if el:
                substrings.insert(len(substrings) // 2, el)

for color in set(secondary_colors.keys()).intersection(result):
    if not secondary_colors[color].issubset(result):
        result.remove(color)

print(result)


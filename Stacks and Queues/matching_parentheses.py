data = input()

counter = []

for i in range(len(data)):
    char = data[i]
    if char == '(':
        counter.append(i)
    elif char == ')':
        last = counter.pop()
        print(data[last:i + 1])
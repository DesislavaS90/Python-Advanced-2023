n = int(input())

unique_names = {input() for _ in range(n)}

for name in unique_names:
    print(name)



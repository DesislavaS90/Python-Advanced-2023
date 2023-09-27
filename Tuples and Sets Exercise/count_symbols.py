text = input()

symbols_count = {}

for el in text:
    if el not in symbols_count:
        symbols_count[el] = 0
    symbols_count[el] += 1

for element, count in sorted(symbols_count.items()):
    print(f'{element}: {count} time/s')

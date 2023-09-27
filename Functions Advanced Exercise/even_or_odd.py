def even_odd(*args):
    result = []
    command = args[-1]
    numbers = [int(x) for x in args[:-1]]

    for x in numbers:
        if command == 'even' and x % 2 == 0:
            result.append(x)

        elif command == 'odd' and x % 2 != 0:
            result.append(x)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
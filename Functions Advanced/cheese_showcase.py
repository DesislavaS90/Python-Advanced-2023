def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for item in sorted_dict:
        result.append(item[0])
        result += sorted(item[1], reverse=True)

    return '\n'.join(map(str, result))


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)




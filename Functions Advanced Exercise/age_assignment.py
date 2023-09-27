def age_assignment(*args, **kwargs):

    result = []

    for key in kwargs.items():
        for name in args:
            if key[0] in name:
                result.append(f'{name} is {key[1]} years old.')
    return '\n'.join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
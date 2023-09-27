def concatenate(*args, ** kwargs):
    text = ''.join(args)

    for k in kwargs:
        if k in text:
            text = text.replace(k, kwargs[k])
    return text


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

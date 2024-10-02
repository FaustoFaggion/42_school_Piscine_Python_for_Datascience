
def ft_filter(func, iterable):

    result: list = []
    for item in iterable:
        if func(item):
            result.append(item)

    return result
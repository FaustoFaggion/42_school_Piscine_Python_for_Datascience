
def filterstring(text: list, n: int):

    return [x for x in text if len(x) > int(n)]
    
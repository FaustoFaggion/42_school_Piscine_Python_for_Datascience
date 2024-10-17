

def square(x: int | float) -> int | float:
    return x ** 2

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, func) -> object:
    count = 0
    def inner() -> float:
        # Declare count as nonlocal to modify the outer scope variable
        nonlocal count
        if count == 0:
            count = x
        count = func(count)
        return count

    return inner

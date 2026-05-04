from collections.abc import Callable


def square(x: int | float) -> int | float:
    return x**2


def pow(x: int | float) -> int | float:
    return x**x


def outer(
    x: int | float, function: Callable[[int | float], float]
) -> Callable[[], float]:

    count = 0

    def inner() -> float:
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count

    return inner

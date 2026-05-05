from collections.abc import Callable


def square(x: int | float) -> int | float:
    """Return the square of a number"""
    return x**2


def pow(x: int | float) -> int | float:
    """Return a number X raised to the power of X."""
    return x**x


def outer(
    x: int | float, function: Callable[[int | float], float]
) -> Callable[[], float]:
    """Decorate a function to sequentially
    apply _function_ to the last returned value, starting from _x_."""
    count = 0

    def inner() -> float:
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count

    return inner

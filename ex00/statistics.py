import math
from typing import Literal


def __mean(arr: list[float]):
    """Return the mean value of an array of numbers"""
    return sum(arr) / len(arr)


def __median(arr: list[float]):
    """Return the median value of an array of numbers"""
    if not len(arr) & 1:
        return arr[(len(arr) + 1) // 2]
    else:
        return arr[len(arr) // 2]


def __quartile(arr: list[float]):
    """Return the first and third quartiles of an array of numbers"""
    q: list[float] = [0, 0]
    if not len(arr) & 1:
        q[0] = arr[(len(arr) + 1) // 4]
        q[1] = arr[math.floor((len(arr) + 1) * 0.75)]
    else:
        q[0] = arr[(len(arr)) // 4]
        q[1] = arr[math.floor((len(arr)) * 0.75)]
    return q


def __var(arr: list[float]):
    """Return the variance value for an array of numbers"""
    m = __mean(arr)
    var = (
        sum(
            map(
                lambda x: (x - m) ** 2,
                arr,
            )
        )
    ) / len(arr)

    return var


def __std(arr: list[float]):
    """Return the standrd deviation of an array of numbers"""
    return math.sqrt(__var(arr))


def ft_statistics(
    *args: float | int,
    **kwargs: Literal["mean", "median", "quartile", "std", "var"]
) -> None:
    """Print the mean, median, first and third quartile, standard deviation
    and variance of an array of numbers. Which data to print can be chosen
    by passing the name of the operation as a value of any keyword argument.
    The name of the keyword arguments does not matter."""
    if any(filter(lambda i: not isinstance(i, (int, float)), args)):
        print("ERROR")
        return
    for op in filter(
        lambda x: x in ["mean", "median", "quartile", "std", "var"],
        kwargs.values(),
    ):
        if len(args) == 0:
            print("ERROR")
            continue
        print(op, ":", end=" ")

        print(
            {
                "mean": __mean,
                "median": __median,
                "quartile": __quartile,
                "std": __std,
                "var": __var,
            }[op](sorted([*map(float, args)]))
        )

from typing import Any


def callLimit(limit: int):
    """Decorate a function or a class to limit the
    number of call allowed to it."""
    count = 0

    def callLimiter(function: Any):
        """Intermedirary function, allowing the use of
        parameters with the decorator."""

        def limit_function(*args: Any, **kwds: Any):
            """Limit the number of calls to function to limit."""
            nonlocal count, limit
            if count == limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter

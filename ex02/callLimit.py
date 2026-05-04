from typing import Any


def callLimit(limit: int):
    count = 0

    def callLimiter(function: Any):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count, limit
            if count == limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter

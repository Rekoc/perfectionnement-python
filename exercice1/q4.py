import timeit
from functools import partial
from typing import Callable


def measure_execution_time(
    x: int, method: Callable, *args, **kwargs
) -> float:
    t = timeit.Timer(
        partial(method, *args, **kwargs)
    )
    return t.timeit(x)
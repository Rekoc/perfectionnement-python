import timeit
from functools import partial
from typing import Callable, List


# def measure_execution_time_with_average(
#     x: int, y: int, method: Callable,
#     *args, **kwargs
# ) -> float:

#     def average(l: List[float]) -> float:
#         return sum(l) / len(l)

#     t = timeit.Timer(
#         partial(method, *args, **kwargs)
#     )
#     return average(
#         [t.timeit(x) for i in range(y)]
#     )

def measure_execution_time_with_average(
    x: int, y: int, method: Callable,
    *args, **kwargs
) -> float:

    def average(l: List[float]) -> float:
        return sum(l) / len(l)

    t = timeit.Timer(
        partial(method, *args, **kwargs)
    )
    return average(
        t.repeat(y, x)
    )
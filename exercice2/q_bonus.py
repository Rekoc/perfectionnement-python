import time
from datetime import datetime
from typing import Callable


def log_execution_time_with_path(path: str):
    def inner_function(method: Callable):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = method(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            with open(path, "a") as log_file:
                log_file.write(
                    f"{datetime.now()}\tMethod {method.__name__}({args}, {kwargs} took : {total_time}\n"
                )
            return result
        return wrapper
    return inner_function
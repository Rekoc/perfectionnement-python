import time
from datetime import datetime
from pathlib import Path
from typing import Callable


BASE_DIR = Path(__file__).resolve().parent.parent
PATH_TO_LOG_FILE = f"{BASE_DIR}/statics/exercice1_q1.txt"

def log_execution_time(method: Callable):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = method(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        with open(PATH_TO_LOG_FILE, "a") as log_file:
            log_file.write(
                f"{datetime.now()}\tMethod {method.__name__}({args}, {kwargs} took : {total_time}\n"
            )
        return result
    return wrapper
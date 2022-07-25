from typing import Tuple
import random
from pprint import pprint


def get_list_of_random_int(x: int, min: int, max: int) -> Tuple[int]:
    return tuple(random.randint(min, max) for i in range(x))

if __name__ == '__main__':
    pprint(
        get_list_of_random_int(10, 1, 10000000)
    )
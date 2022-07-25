from typing import Sequence, Tuple


def diff_set(s1: Sequence[int], s2: Sequence[int]) -> Tuple[int]:
    s1 = set(s1)
    s2 = set(s2)
    return tuple(s1.symmetric_difference(s2))
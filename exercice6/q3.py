import numpy as np
from .q1 import RegexLog
from typing import Union
Number = Union[int, float, np.number]


class LogStats:
    def __new__(cls, *args):
        for item in args:
            if not isinstance(item, RegexLog):
                raise ValueError(f"Instance '{item}' is not of type {RegexLog}")
        return super().__new__(cls)

    def __init__(self, *args):
        self.stats = args
        self.nb_lines = self.counting_lines(
            RegexLog.PATH_TO_LOG_FILE
        )

    def print_stats(self):
        print(f"Your log file has {self.nb_lines}.")
        for item in self.stats:
            nb_items = len(item.logs)
            print(
                f"{item} has matched {nb_items} times ({self.percentage(nb_items, self.nb_lines)} %)"
            )

    @property
    def logs_stats(self):
        return {str(item): len(item.logs) for item in self.stats}

    @staticmethod
    def counting_lines(path: str) -> int:
        with open(path, "r") as file:
            for count, line in enumerate(file):
                pass
        return count + 1

    @staticmethod
    def percentage(x: Number, y: Number) -> int:
        return round((x / y) * 100, 2)
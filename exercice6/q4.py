from matplotlib import pyplot as plt
import numpy as np
from .q3 import LogStats


class LogGraph(LogStats):
    def display(self):
        x = self.logs_stats.keys()
        y = self.logs_stats.values()

        plt.bar(x, y, align = 'center')
        plt.title("Logs analyses")
        plt.ylabel("Number of logs")
        plt.xlabel("Log level")

        plt.show()
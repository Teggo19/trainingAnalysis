import matplotlib.pyplot as plt
import numpy as np


def showGraphWithDataPoints(graph, datapoints, title=""):

    fig, ax1 = plt.subplots()
    ax1.plot(graph, color="red")
    ax2 = ax1.twinx()
    x = np.arange(len(datapoints))
    ax2.bar(x, datapoints, 1, label="Data points", alpha=0.4)
    ax1.set_ylabel("form")
    ax2.set_ylabel("numer of samples")
    fig.legend()
    ax1.set_title(title)
    plt.show()

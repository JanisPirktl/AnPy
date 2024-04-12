import matplotlib.pyplot as plt
import numpy as np


def teilsummen(n, p):
    k = np.arange(1, n + 1)
    return np.cumsum(1 / k ** p)


def code1(n):

    p_werte = np.arange(0.85, 1.25, 0.05)

    for p in p_werte:
        teilsummen_werte = teilsummen(n, p)
        color = "red" if p > 1 else "blue"
        plt.plot(teilsummen_werte, color=color)

    plt.plot([], [], label="p <= 1", color="blue")
    plt.plot([], [], label="p > 1", color="red")

    plt.xlabel("Anzahl Summenglieder")
    plt.ylabel("Teilsumme der Summenglieder")
    plt.title("p-Werte zwischen 0.85 und 1.2")

    plt.legend(framealpha=1)
    plt.grid(True)
    plt.show()


code1(100000)




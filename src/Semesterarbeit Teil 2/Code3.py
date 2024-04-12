import math

import numpy as np
import matplotlib.pyplot as plt


def teilsummen(n, p):
    k = np.arange(1, n + 1)
    return np.cumsum(1 / np.power(k, p))


def code3(n):

    p_werte = np.arange(-2, 0.5, 0.5)

    for p in p_werte:
        teilsummen_werte = teilsummen(n, p)
        plt.plot(teilsummen_werte, label=f'p = {round(p, 1)}')

    plt.xlabel('Anzahl Summenglieder')
    plt.ylabel('Teilsumme der Summenglieder')
    plt.title('Wachstumszunahme für negative p-Werte')

    plt.legend(framealpha=1)
    plt.grid(True)
    plt.show()


code3(6)

import numpy as np
import matplotlib.pyplot as plt


def teilsummen(n, p):
    k = np.arange(1, n + 1)
    return np.cumsum(1 / k**p)


def code4(n):

    p_werte = np.arange(1.5, 4, 0.5)
    print(p_werte)

    for p in p_werte:
        teilsummen_werte = teilsummen(n, p)
        plt.plot(teilsummen_werte, label=f'p = {round(p, 1)}')

    plt.xlabel('Anzahl Summenglieder')
    plt.ylabel('Teilsumme der Summenglieder')
    plt.title('Konvergenzgeschwindigkeit für verschiedene p-Werte')

    plt.legend(loc='center right', framealpha=1, borderpad=2)
    plt.grid(True)
    plt.show()


code4(100)

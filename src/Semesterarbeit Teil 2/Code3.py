import numpy as np
import matplotlib.pyplot as plt


def teilsummen1(n, p):
    k = np.arange(1, n + 1)
    return np.cumsum(1 / k**p)


def code3(n):

    p_werte = [1.1, 1.5, 2, 3]

    for p in p_werte:
        teilsummen = teilsummen1(n, p)
        plt.plot(teilsummen, label=f'p = {p}')

    plt.xlabel('Anzahl Summenglieder')
    plt.ylabel('Teilsumme der Summenglieder')
    plt.title('Konvergenzgeschwindigkeit für verschiedene p')
    plt.legend()
    plt.grid(True)
    plt.show()


code3(100)

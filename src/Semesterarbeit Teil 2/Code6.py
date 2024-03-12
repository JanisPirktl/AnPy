import numpy as np
import matplotlib.pyplot as plt


def harmonische_reihe(n):
    return np.cumsum(1 / np.arange(1, n + 1))


def konstanter_aufwand(n):
    return np.ones(n)


def logarithmischer_aufwand(n):
    return np.log(np.arange(1, n + 1))


def linearer_aufwand(n):
    return np.arange(1, n + 1)


def quasi_linearer_aufwand(n):
    k = np.arange(1, n + 1)
    return k * np.log(k)


def code6(n):
    plt.plot(harmonische_reihe(n), label='Harmonische Reihe')
    plt.plot(konstanter_aufwand(n), label='Konstanter Aufwand')
    plt.plot(logarithmischer_aufwand(n), label='Logarithmischer Aufwand')
    plt.plot(linearer_aufwand(n), label='Linearer Aufwand')
    plt.plot(quasi_linearer_aufwand(n), label='Quasi-Linearer Aufwand')

    plt.xlabel('n')
    plt.ylabel('Aufwand')
    plt.title('Komplexitäts-Klassen')
    plt.legend()
    plt.grid(True)
    plt.show()


code6(6)

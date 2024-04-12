import numpy as np
import matplotlib.pyplot as plt


def teilsumme(n, p):
    k = np.arange(1, n + 1)
    return np.sum(1 / k ** p)


def code2(n):

    p_werte = np.arange(0.5, 2.1, 0.1)
    teilsumme_werte = []

    for p in p_werte:
        teilsumme_werte.append(teilsumme(n, p))

    plt.plot(p_werte, teilsumme_werte, marker='o', linestyle='-', color='blue')
    plt.axvline(x=1, color='green', linestyle='--', label='Grenze p=1')
    plt.xlabel('Exponent p')
    plt.ylabel(f'Teilsumme der ersten {n} Terme')
    plt.title("p-Werte zwischen 0.5 und 2")

    plt.legend(framealpha=1)
    plt.grid(True)
    plt.show()


code2(10000)

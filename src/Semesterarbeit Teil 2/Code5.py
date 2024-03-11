import numpy as np
import matplotlib.pyplot as plt


def folge_glieder(n, p):
    k = np.arange(1, n + 1)
    folge_werte = 1 / k**p
    return folge_werte


def code5(n):
    p_werte = [1.1, 1.5, 2, 3, 5]
    print(p_werte)

    for p in p_werte:
        folge_werte = folge_glieder(n, p)
        plt.plot(folge_werte, label=f'p = {round(p, 1)}')

    plt.xlabel('Anzahl Folgeglieder')
    plt.ylabel('Glied der Folge')
    plt.title('Konvergenzgeschwindigkeit für verschiedene p-Werte')
    plt.legend(loc='center right', framealpha=1, borderpad=2)
    plt.grid(True)
    plt.show()


code5(10)
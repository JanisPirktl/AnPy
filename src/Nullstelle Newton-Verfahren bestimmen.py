import numpy as np


def newton_raphson(f, df, x0, tol=1e-6, max_iter=1000):
    """
    Bestimmt die Nullstelle einer Funktion f mithilfe des Newton-Raphson-Verfahrens.

    Parameter:
    f : Funktion
        Die Funktion, deren Nullstelle bestimmt werden soll.
    df : Funktion
        Die Ableitung der Funktion f.
    x0 : float
        Anfangswert für die Iteration.
    tol : float
        Toleranz für das Abbruchkriterium.
    max_iter : int
        Maximale Anzahl der Iterationen.

    Rückgabe:
    float
        Die geschätzte Nullstelle der Funktion f.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(fx) < tol:
            print(f"Nullstelle nach {i + 1} Iterationen gefunden: x = {x}")
            return x

        if dfx == 0:
            raise ValueError("Ableitung ist null. Das Verfahren kann nicht fortgesetzt werden.")

        x = x - fx / dfx

    raise ValueError("Maximale Anzahl an Iterationen erreicht. Keine Nullstelle gefunden.")


# Beispiel: Nullstelle der Funktion f(x) = x^2 - 2
def f(x):
    return x ** 2 - 2


def df(x):
    return 2 * x


# Startwert
x0 = 1.0

# Berechnung der Nullstelle
nullstelle = newton_raphson(f, df, x0)
print("Geschätzte Nullstelle:", nullstelle)

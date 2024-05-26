import scipy.integrate as integrate


# Definiere die Funktion, die integriert werden soll
def funktion(x):
    return x**4/4 + 2*x**3/3 - x**2/2 - 2*x  # Beispiel: quadratische Funktion


# Definiere das Intervall
a = -1  # Untere Grenze
b = 1  # Obere Grenze


ergebnis, fehler = integrate.quad(funktion, a, b)

print(f"Das Integral von {a} bis {b} ist: {ergebnis}")

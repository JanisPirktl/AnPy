import math
import matplotlib.pyplot as plt
import Funktionen as Functions
import sympy as sp


# Die zu integrierende Funktion
def f(x):
    return math.pi / x


x_values = list(range(2, 20, 2))
y_values_sekanten = []
y_values_tangenten = []
y_values_simpson = []

# Intervallgrenzen
a = 1
b = 2

# Berechnen des exakten Wertes mit SymPy
x = sp.Symbol('x')
exact_integral = sp.integrate(sp.pi / x, (x, a, b)).evalf()

print(f"Exakter Wert des Integrals: {exact_integral}")
print()

for n in range(2, 20, 2):
    approx_sekanten = Functions.sekanten_trapez_regel(f, a, b, n)
    y_values_sekanten.append(approx_sekanten)
    print(f"\nAnzahl der Unterintervalle: {n}")
    print(f"Sekanten-Trapez-Regel: {approx_sekanten} (Fehler: {abs(exact_integral - approx_sekanten)})")
print()

for n in range(2, 20, 2):
    approx_tangenten = Functions.tangenten_trapez_regel(f, a, b, n)
    y_values_tangenten.append(approx_tangenten)
    print(f"\nAnzahl der Unterintervalle: {n}")
    print(f"Tangenten-Trapez-Regel: {approx_tangenten} (Fehler: {abs(exact_integral - approx_tangenten)})")
print()

for n in range(2, 20, 2):
    approx_simpson = Functions.simpson_regel(f, a, b, n)
    y_values_simpson.append(approx_simpson)
    print(f"\nAnzahl der Unterintervalle: {n}")
    print(f"Simpson-Regel: {approx_simpson} (Fehler: {abs(exact_integral - approx_simpson)})")

plt.title('Vergleich der Genauigkeit der Approximationen')
plt.xlabel("Anzahl der Unterintervalle")
plt.ylabel("Approximation")
plt.plot(x_values, y_values_sekanten, label='Sekanten-Trapez-Regel', color='red')
plt.plot(x_values, y_values_tangenten, label='Tangenten-Trapez-Regel', color='green')
plt.plot(x_values, y_values_simpson, label='Simpson-Regel', color='blue')
plt.axhline(y=exact_integral, label="Exakter Wert des Integrals", color='yellow', linestyle='--')
plt.legend()
plt.show()

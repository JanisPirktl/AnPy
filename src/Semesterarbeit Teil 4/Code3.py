import matplotlib.pyplot as plt
import Funktionen as Fnk
import sympy as sp
from math import pi


def f(x):
    return sp.cos(x)


a = -pi/2
b = pi/2

x = sp.symbols('x')

exact_value = sp.integrate(f(x), (x, a, b)).evalf()

num_stripes = list(range(2, 22, 2))

results = {
    'n': [],
    'sekanten_trapez': [],
    'tangenten_trapez': [],
    'simpson': [],
    'sekanten_fehler': [],
    'tangenten_fehler': [],
    'simpson_fehler': []
}

for n in num_stripes:
    sekanten_result = Fnk.sekanten_trapez_regel(f, a, b, n)
    tangenten_result = Fnk.tangenten_trapez_regel(f, a, b, n)
    simpson_result = Fnk.simpson_regel(f, a, b, n)

    results['n'].append(n)
    results['sekanten_trapez'].append(sekanten_result)
    results['tangenten_trapez'].append(tangenten_result)
    results['simpson'].append(simpson_result)
    results['sekanten_fehler'].append(abs(sekanten_result - exact_value))
    results['tangenten_fehler'].append(abs(tangenten_result - exact_value))
    results['simpson_fehler'].append(abs(simpson_result - exact_value))

print(f"Exakter Wert des Integrals: {exact_value}")
print()

for i in range(len(num_stripes)):
    print(f"n = {results['n'][i]}")
    print(f"Sekanten-Trapez-Ergebnis: {results['sekanten_trapez'][i]}, Fehler: {results['sekanten_fehler'][i]}")
    print(f"Tangenten-Trapez-Ergebnis: {results['tangenten_trapez'][i]}, Fehler: {results['tangenten_fehler'][i]}")
    print(f"Simpson-Ergebnis: {results['simpson'][i]}, Fehler: {results['simpson_fehler'][i]}")
    print("-" * 50)


plt.figure(figsize=(12, 8))
plt.plot(results['n'], results['sekanten_fehler'], label='Sekanten-Trapez-Fehler', color='blue')
plt.plot(results['n'], results['tangenten_fehler'], label='Tangenten-Trapez-Fehler', color='green')
plt.plot(results['n'], results['simpson_fehler'], label='Simpson-Fehler', color='red')
plt.xlabel('Anzahl der Streifen (n)')
plt.ylabel('Fehler')
plt.title('Vergleich der Fehler bei numerischer Integration')
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(12, 8))
plt.plot(results['n'], results['sekanten_trapez'], label='Sekanten-Trapez-Ergebnis', color='blue')
plt.plot(results['n'], results['tangenten_trapez'], label='Tangenten-Trapez-Ergebnis', color='green')
plt.plot(results['n'], results['simpson'], label='Simpson-Ergebnis', color='red')
plt.axhline(y=exact_value, color='orange', linestyle='--', label='Exakter Wert')
plt.xlabel('Anzahl der Streifen (n)')
plt.ylabel('Integralergebnis')
plt.title('Vergleich der Integralergebnisse')
plt.legend()
plt.grid(True)
plt.show()

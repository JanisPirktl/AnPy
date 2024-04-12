import sympy as sp

# Definiere die Variable x
x = sp.symbols('x')

# Definiere die Funktion, zum Beispiel f(x) = x^2
f = x**2

# Berechne die erste Ableitung der Funktion
f_prime = sp.diff(f, x)

# Wähle den Punkt a, an dem die Tangente berechnet werden soll
a = 2  # Beispielwert für a

# Berechne die Steigung der Tangente an der Stelle x = a
slope = f_prime.subs(x, a)

# Berechne den y-Wert der Funktion an der Stelle x = a
y_at_a = f.subs(x, a)

# Stelle die Gleichung der Tangente auf: T(x) = f'(a)(x - a) + f(a)
T = slope * (x - a) + y_at_a

# Zeige die Ableitung der Funktion und die Gleichung der Tangente an
print(f"Die erste Ableitung der Funktion ist: {f_prime}")
print(f"Die Gleichung der Tangente an der Stelle x = {a} ist: T(x) = {T}")

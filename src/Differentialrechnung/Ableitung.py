from sympy import symbols, diff

# Definieren der Variablen und der Funktion
x = symbols('x')
y = symbols('y')
funktion = (x**4 + 5)**7

# Berechnen der ersten Differentialrechnung der Funktion
ableitung = diff(funktion, x)

print(ableitung)

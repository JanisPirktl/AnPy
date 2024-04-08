from sympy import symbols, diff

# Definieren der Variablen und der Funktion
x = symbols('x')
funktion = 3 * x**5

# Berechnen der ersten Differentialrechnung der Funktion
ableitung = diff(funktion, x)

print(ableitung)

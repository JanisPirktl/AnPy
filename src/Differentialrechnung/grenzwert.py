import sympy as sp

x = sp.Symbol('x')

#grenzwert von      sin(x) / x

a = sp.limit(sp.sin(x) / x, x, 0)

print(a)

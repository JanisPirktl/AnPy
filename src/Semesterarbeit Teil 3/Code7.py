import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import sympy as sp

# Symbol
x = sp.symbols('x')

# Function
f = sp.sin(x) + sp.cos(2 * x)

# Derivation
df = sp.diff(f, x)
ddf = sp.diff(df, x)
f_func = sp.lambdify(x, f, 'numpy')
df_func = sp.lambdify(x, df, 'numpy')
ddf_func = sp.lambdify(x, ddf, 'numpy')

# Finer grid for display
x_fine = np.linspace(0, 2 * np.pi, 100)
y_fine = f_func(x_fine)
ddy_fine = ddf_func(x_fine)

# Datapoints
x_data = [x_fine[0]]
is_positive = ddy_fine[0] > 0
isGoingUp = y_fine[0] < y_fine[1]

for i in range(1, len(ddy_fine) - 1):
    if y_fine[i] > y_fine[i-1] and y_fine[i] > y_fine[i+1] and isGoingUp:
        x_data.append(x_fine[i])
        isGoingUp = False
    elif y_fine[i] < y_fine[i-1] and y_fine[i] < y_fine[i+1] and not isGoingUp:
        x_data.append(x_fine[i])
        isGoingUp = True
    elif (ddy_fine[i] > 0 and not is_positive) or (ddy_fine[i] < 0 and is_positive):
        x_data.append((x_fine[i-1] + x_fine[i]) / 2)
        is_positive = not is_positive

x_data.append(x_fine[-1])
y_data = [f_func(x) for x in x_data]

# Spline
cs = CubicSpline(x_data, y_data, bc_type='natural')
y_spline = cs(x_fine)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(x_fine, y_fine, label='Exakte Kurve (sin(x) + cos(2x))')
plt.plot(x_data, y_data, 'o', label='Stützpunkte')
plt.plot(x_fine, y_spline, '--', label='Kubischer Spline')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stützstellen an lokalen Maxima und Minima sowie Wendepunkte')
plt.grid(True)
plt.show()

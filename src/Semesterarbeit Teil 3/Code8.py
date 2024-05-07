import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
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

# Mean squared error
mse = np.mean((y_fine - y_spline)**2)

# Mean absolute error
mae = np.mean(abs(y_fine - y_spline))

# Maximum error
max_error = np.max(np.abs(y_fine - y_spline))

# Plot
plt.figure(figsize=(10, 5))
plt.plot(x_fine, np.abs(y_fine - y_spline), label='Absoluter Fehler')
plt.axhline(y=max_error, label="Maximaler Fehler: {:.3f}".format(max_error), color='green', linestyle='--')
plt.axhline(y=mae, label="Mittlerer absoluter Fehler: {:.3f}".format(mae), color='orange', linestyle='--')
plt.axhline(y=mse, label="Mittlerer quadratischer Fehler: {:.3f}".format(mse), color='red', linestyle='--')
plt.title('Fehlerquantifizierung für Stützstellen an lokalen Maxima und Minima sowie Wendepunkte')
plt.ylim(0, 0.6)
plt.legend(loc='center')
plt.show()

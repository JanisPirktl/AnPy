import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


# Function
def f(x):
    return np.sin(x) + np.cos(2 * x)


# Datapoints
x_data = np.linspace(0, 2 * np.pi, 6)
y_data = f(x_data)

# Finer grid for display
x_fine = np.linspace(0, 2 * np.pi, 100)
y_fine = f(x_fine)

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
plt.title('Approximation einer trigonometrischen Funktion mit kubischen Splines')
plt.grid(True)
plt.show()

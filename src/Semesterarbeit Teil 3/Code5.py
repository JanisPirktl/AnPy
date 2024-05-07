import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


# Function
def f(x):
    return np.sin(x) + np.cos(2 * x)


# Finer grid for display
x_fine = np.linspace(0, 2 * np.pi, 100)
y_fine = f(x_fine)


# Datapoints
x_data = [x_fine[0]]
isGoingUp = y_fine[0] < y_fine[1]

for i in range(1, len(y_fine) - 1):
    if y_fine[i] > y_fine[i-1] and y_fine[i] > y_fine[i+1] and isGoingUp:
        x_data.append(x_fine[i])
        isGoingUp = False
    elif y_fine[i] < y_fine[i-1] and y_fine[i] < y_fine[i+1] and not isGoingUp:
        x_data.append(x_fine[i])
        isGoingUp = True

x_data.append(x_fine[-1])
y_data = [f(x) for x in x_data]


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
plt.title('Approximation mit Stützstellen an lokalen Maxima und Minima')
plt.grid(True)
plt.show()

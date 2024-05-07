import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

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
plt.title('Fehler zwischen exakter Kurve und Spline-Approximation')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Function to integrate
def f(x):
    return np.sin(x)

# Trapezoidal Rule Function
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    sum = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        sum += f(a + i * h)
    return sum * h

# Parameters
a = 0    # Lower limit of integration
b = np.pi  # Upper limit of integration
n = 100  # Number of intervals

# Calculate the integral
integral = trapezoidal_rule(a, b, n)
print(f"Approximate integral using the trapezoidal rule: {integral}")

# Visualization
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, label='f(x) = sin(x)')
plt.fill_between(x, 0, y, alpha=0.2, label='Area under f(x)')
plt.title("Trapezoidal Rule Integration")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 4*x**5 - 3*x**3 + 2*x - 9


def true_derivative(x):
    return 20*x**4 - 9*x**2 + 2

x = np.linspace(-1, 1, 100)
h = 0.15

FDD = (f(x + h) - f(x)) / h

BDD = (f(x) - f(x - h)) / h

CDD = (f(x + h) - f(x - h)) / (2*h)

true_deriv = true_derivative(x)

plt.figure(figsize=(10, 6))
plt.plot(x, FDD, label='Forward Difference Derivative (FDD)', linestyle='--', color='blue')
plt.plot(x, BDD, label='Backward Difference Derivative (BDD)', linestyle='--', color='red')
plt.plot(x, CDD, label='Central Difference Derivative (CDD)', linestyle='--', color='green')
plt.plot(x, true_deriv, label='True Derivative', color='black')

plt.title('Comparison of FDD, BDD, CDD with True Derivative')
plt.xlabel('x')
plt.ylabel("Derivative")
plt.legend()
plt.grid(True)
plt.show()

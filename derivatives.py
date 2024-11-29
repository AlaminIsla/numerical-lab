import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 7 * np.exp(0.5 * x)


def f_prime(x):
    return 3.5 * np.exp(0.5 * x)


def fdd(f, x, h):
    return (f(x + h) - f(x)) / h


# Define step sizes
h = [0.3, 0.15, 0.1, 0.05, 0.01, 0.001]

# True derivative value at x = 2
true_value = 9.513986399606658

x = 2
fdd_errors = []
for i in h:
    approx_value = fdd(f, x, i)
    arte = (abs(true_value - approx_value)) * 100 / true_value
    fdd_errors.append(arte)
    print("h = ", i, "; derivative = ", approx_value, "; ARTE = ", arte, "%")


# Backward Difference (BDD)
def bdd(f, x, h):
    return (f(x) - f(x - h)) / h


bdd_errors = []
for i in h:
    approx_value = bdd(f, x, i)
    arte = (abs(true_value - approx_value)) * 100 / true_value
    bdd_errors.append(arte)
    print("h = ", i, "; derivative = ", approx_value, "; ARTE = ", arte, "%")


# Central Difference (CDD)
def cdd(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


cdd_errors = []
for i in h:
    approx_value = cdd(f, x, i)
    arte = (abs(true_value - approx_value)) * 100 / true_value
    cdd_errors.append(arte)
    print("h = ", i, "; derivative = ", approx_value, "; ARTE = ", arte, "%")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(h, fdd_errors, label='FDD', marker='o')
plt.plot(h, bdd_errors, label='BDD', marker='^')
plt.plot(h, cdd_errors, label='CDD', marker='x')

plt.xlabel('h', fontsize=14)
plt.ylabel(r'$ |\epsilon_t| $ (%)', fontsize=14)
plt.title('Error vs. Step Size for Differentiation Methods', fontsize=16)
plt.xscale('log')  # Optional: Use logarithmic scale for better visualization
plt.yscale('log')
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt


#  -4x + cos x + 2 =0

def non_linear_func(x):
    return -4 * x + np.cos(x) + 2


x = np.linspace(0, 5, 1000)
y = non_linear_func(x)

plt.plot(x, y)
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")

plt.grid()
plt.show()


def f_prime(x):
    return -4 - np.sin(x)


def area(x_prev, x_pres):
    return abs((x_pres - x_prev) / x_pres) * 100


def newton_raphson(f, f_prime, x0, error_tol, max_iter):
    x = x0
    x_prev = None
    error = 1e10
    for i in range(max_iter):
        x = x - f(x) / f_prime(x)
        if x_prev is not None:
            error = area(x_prev, x)
            if error < error_tol:
                print("converged")
                print(f"Error after iteration {i + 1}: {error}")
                return x
        x_prev = x
        print(f"Value of x after iteration {i + 1}: {x}")
        print(f"Error after iteration {i + 1}: {error}")
    return x


x = newton_raphson(non_linear_func, f_prime, 0.1, 0.01, 100)

print(x)

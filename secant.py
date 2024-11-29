import numpy as np


def non_linear_func(x):
    return -4 * x + np.cos(x) + 2


def area(x_prev, x_pres):
    return abs((x_pres - x_prev) / x_pres) * 100


def secant_method(f, x0, x1, error_tol, max_iter):
    error = 1e10
    for i in range(max_iter):

        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            print("Division by zero error in the Secant method")
            return None

        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        error = area(x1, x_new)

        if error < error_tol:
            print("Converged")
            print(f"Root found after iteration {i + 1}: {x_new}")
            print(f"Error after iteration {i + 1}: {error}")
            return x_new

        x0 = x1
        x1 = x_new

        print(f"Iteration {i + 1}: x = {x_new}")
        print(f"Error after iteration {i + 1}: {error}")
        print()

    return x_new


# Initial guesses
x0 = 0.45
x1 = 0.5

# Tolerance for error and maximum iterations
error_tol = 1e-6
max_iter = 100

# Call the Secant method
root = secant_method(non_linear_func, x0, x1, error_tol, max_iter)

print(f"Final root: {root}")
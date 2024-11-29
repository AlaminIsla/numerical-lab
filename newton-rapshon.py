import numpy as np
import matplotlib.pyplot as plt


def non_linear_func(x):
    return x ** 3 - 0.165 * x ** 2 + 3.993 * 10 ** (-4)


x = np.linspace(0, 0.11, 1000)
y = non_linear_func(x)

plt.plot(x, y)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid()
plt.show()


def f_prime(x):
    return 3 * x ** 2 - 0.33 * x


def arae(x_prev, x_pres):  # function of absolute relative approximation error
    return abs((x_pres - x_prev) / x_pres) * 100


def plot(f, f_prime, x0, new_x):
    x = np.linspace(0, 0.11, 1000)
    y = f(x)

    plt.plot(x, y, 'b', label='f(x)', linewidth=3)  # drawing the curve at each iteration
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.axvline(x=new_x, color='g', linestyle='--', label='$x_{i+1}$')  # plot the new point of x vertically

    # draw the tangent line for
    x1 = np.linspace(x0 - 0.05, x0 + 0.05, 100)
    y1 = f_prime(x0) * (x1 - x0) + f(x0)  # equation of drawing linear line

    plt.plot(x1, y1, 'r', label='f\'(x)')  # drawing the slope at w.r.t the point x0
    plt.axvline(x=x0, color='orange', linestyle='--', label='$x_{i}$')
    plt.scatter(x0, f(x0), color='r')  # speicify the point x0,f(x0) in the graph
    plt.grid()
    plt.legend()
    plt.show()


def newton_raphson(f, f_prime, x0, error_tol, max_iter):
    x = x0
    x_prev = None
    error = 1e10
    for i in range(max_iter):
        x = x - f(x) / f_prime(x)
        if x_prev is not None:
            plot(f, f_prime, x_prev, x)
            error = arae(x_prev, x)
            if error < error_tol:
                print("Converged")
                print(f"Error after iteration {i + 1}: {error}")
                return x
        x_prev = x
        print(f"Value of x after iteration {i + 1}: {x}")
        print(f"Error after iteration {i + 1}: {error}")
        print()
    return x

newton_raphson(non_linear_func, f_prime, 0.1, 0.01, 100)
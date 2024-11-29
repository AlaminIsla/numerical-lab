import numpy as np
import matplotlib.pyplot as plt


def derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / (h)


def f(x):
    return 7 * np.exp(0.5 * x)


f(2)
derivative(f, 2, h=0.3)

true_value = 9.513986399606658
h = [0.3, 0.15, 0.1, 0.05, 0.01, 0.001]
x = 2
for i in h:
    approx_value = derivative(f, x, i)
    # print("h = ", i, "; derivative = ", approx_value, "; true error = ", abs(true_value - approx_value))

h = [0.3, 0.15, 0.1, 0.05, 0.01, 0.001]
x = 2
for i in h:
    approx_value = derivative(f, x, i)
    print("h = ", i, "; derivative = ", approx_value, "; RTE = ", (abs(true_value - approx_value)) * 100 / true_value,
          "%")

prev_approx = derivative(f, x=2, h=0.3)
print("First approximation: ", prev_approx)
print()

# let the first approximation be for h = 0.3
prev_approx = derivative(f, x=2, h=0.3)
print("First approximation: ", prev_approx)
print()

# let the successive approximations be for decreasing values of h
h = [0.15, 0.1, 0.05, 0.01, 0.001, 0.0001]
for i in h:
    present_approx = derivative(f, x=2, h=i)
    print("Previous approximation for h = ", i, " is: ", prev_approx)
    print("Present approximation for h = ", i, " is: ", present_approx)

    RAE = abs(present_approx - prev_approx) * 100 / present_approx

    print("RAE: ", RAE, "%")
    print()
    prev_approx = present_approx


prev_approx = derivative(f, x=2, h=0.3)


h = [0.15, 0.1, 0.05, 0.01, 0.001, 0.0001]
errors = []
for i in h:
    present_approx = derivative(f, x=2, h=i)
    RAE = abs(present_approx - prev_approx) * 100 / present_approx
    errors.append(RAE)
    prev_approx = present_approx

print("h values: ", h)
print("errors: ", errors)


plt.figure(figsize=(10, 5))
plt.plot(h, errors, marker='x', color='red', linewidth=3, markersize=10)
plt.xlabel("h", fontdict={'fontsize': 15})
plt.ylabel("RAE", fontdict={'fontsize': 15})
plt.title("Relative Approximate Error vs Step Size", fontdict={'fontsize': 20})
plt.show()

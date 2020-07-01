import numpy as np
import matplotlib.pyplot as plt

def df1(x, y): # k = 3
    return y * (1 - 3 * y)


def Euler(df, N, x_end, x_0, y_0, dx):
    # df: differential equation
    # N: Total steps
    # x_end: x's stopping point
    # x_0: Initial x
    # y_0: Initial y(x_0)
    # dx: Step size
    i = 0
    x = [x_0, ]
    Y = [y_0, ]
    while i <= N and x[-1] <= x_end:
        x.append(x[-1] + dx)
        Y.append(Y[-1] + dx * df(x[-2], Y[-1])) # Note: x_i should be the penultimate object in the x list(x_i = x[-2])

    return x, Y


x, Y = Euler(df1, 5 / 1e-6, 5, 0, 0.1, 1e-6)
plt.plot(x, Y, c = 'b')
plt.show()
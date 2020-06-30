import numpy as np
from scipy.misc import derivative

def f(x):
    return np.exp(-x)+np.square(x)-6*x


def Newton(f, i, s):
    x = i # i is the initial x(x_0)
    xn = x - f(x)/derivative(f, x, dx = 1e-6)
    while np.abs(f(x)) >= s: # Exception
        xn = x - f(x) / derivative(f, x, dx = 1e-6)
        x = xn
    return x


print(Newton(f, 1, 1e-6))
print(Newton(f, 5, 1e-6))


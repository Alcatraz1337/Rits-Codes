import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt

def f(x):
    return x * np.exp(-x/2)-np.exp(-x)


def Newton(f, i, s):
    x = i # i is the initial x(x_0)
    xn = x - f(x)/derivative(f, x, dx = 1e-6)
    while np.abs(f(x)) >= s: # Exception
        xn = x - f(x) / derivative(f, x, dx = 1e-6)
        x = xn
    return x

x = np.arange(-2, 10, 0.01)
y = []
for i in x:
    y.append(f(i))
plt.plot(x,y)
plt.show()
print(Newton(f, 1, 1e-6))
print(Newton(f, 10, 1e-10))
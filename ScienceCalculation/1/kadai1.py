import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.cos(x)
plt.plot(x, y)
plt.show()
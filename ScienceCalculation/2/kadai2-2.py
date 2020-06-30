import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

A = np.array([[3, 2], [5, 2]])
plt.figure()
ax = plt.gca()
for i in range(0, 11, 1):
    for j in range(0, 11, 1):
        (x, y) = (0.1 * i, 0.1 * j)
        ax.scatter(x, y,s=4, c='r')
        vec = np.dot(A, (x, y))
        ax.scatter(vec[0], vec[1], c='b')
ax.set_aspect(1)
ax.set_xlim([0, 9])
ax.set_ylim([0, 9])
plt.draw()
plt.show()

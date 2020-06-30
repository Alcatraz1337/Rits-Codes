import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

A = np.array([[3, 2], [5,2]])
print(A)
w, v = la.eig(A)
print(w, v)
plt.figure()
ax = plt.gca()
for i in range(v.shape[1]):
    vec = v[:, i]
    ax.quiver(0,
              0,
              vec[0],
              vec[1],
              angles='xy',
              scale_units='xy',
              scale=1,
              color='blue')
    conVec = np.dot(A, vec)
    print(conVec)
    ax.quiver(0,
              0,
              conVec[0],
              conVec[1],
              angles='xy',
              scale_units='xy',
              scale=1,
              color='red')
ax.set_aspect(1)
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
plt.draw()
plt.show()
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


SampleNum = 100000
sum = 0
inRange = []
outRange = []

for i in range(0,SampleNum):
    x = np.random.rand(1)
    y = np.random.rand(1)

    if (np.square(x) + np.square(y)) < 1:
        sum = sum + 1
        inRange.append(tuple((x, y)))
    else:
        outRange.append(tuple((x, y)))

plt.axis('equal')
plt.scatter(*zip(*inRange), c='r', s=1)
plt.scatter(*zip(*outRange), c='b', s=1)
plt.show()
P = sum * 4 / SampleNum
print(P)
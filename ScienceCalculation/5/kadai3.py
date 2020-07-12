import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


SampleNum = 1000000
sum = 0

for i in range(0,SampleNum):
    x = np.random.rand(1)
    y = np.random.rand(1)

    if (np.square(x) + np.square(y)) < 1:
        sum = sum + 1

P = sum * 4 / SampleNum
print(P)
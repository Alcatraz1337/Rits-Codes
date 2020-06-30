import numpy as np

def manhatannDist(a, b):
    return np.sum(np.abs(a - b))

aa = (1, 1)
dd = (13, 13)
a = np.array(aa)
d = np.array(dd)
dist = manhatannDist(a, d)
print(dist)
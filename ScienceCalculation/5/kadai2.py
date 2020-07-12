import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

sampleNUm = 10000
mu, sigma = 0, 2

rands = np.random.normal(mu, sigma, sampleNUm)
y = st.norm.pdf(rands, mu, sigma)
avg = np.mean(rands)
stdDev = np.std(rands)

print("Average:", avg, " Standard Deviation:", stdDev)

plt.hist(rands, bins=40, density= True) # Histogram
zipped = zip(rands, y)
x, y = zip(*sorted(zipped)) # Sort x, y
plt.plot(x, y, 'r--') # Plot 
plt.show()
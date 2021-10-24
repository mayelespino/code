import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.randn(1000)

plt.figure()
hist1, edges1 = np.histogram(data1, bins=100)
plt.bar(edges1[:-1], hist1, width=edges1[1:]-edges1[:-1])
plt.show()

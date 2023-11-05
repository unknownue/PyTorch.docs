import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))

x = np.arange(15)
y = np.random.rand(15)
y2 = np.random.rand(15)
ax1.scatter(x, y, s=20, edgecolors='k', c='b', label='a')
ax1.scatter(x, y2, s=20, edgecolors='k', c='b', label='b')
ax1.legend()
ax1.set_title('classic')

ax2.scatter(x, y, label='a')
ax2.scatter(x, y2, label='b')
ax2.legend()
ax2.set_title('v2.0')
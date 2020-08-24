import numpy as np
import matplotlib.pyplot as plt

data = np.arange(30).reshape(5, 6)
x = np.linspace(0, 6, 7)
y = 10**np.linspace(0, 5, 6)
X, Y = np.meshgrid(x, y)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4))

ax1.imshow(data, aspect="auto", extent=(0, 6, 1e0, 1e5), interpolation='nearest')
ax1.set_yscale('log')
ax1.set_title('Using ax.imshow')

ax2.pcolormesh(x, y, np.flipud(data))
ax2.set_yscale('log')
ax2.set_title('Using ax.pcolormesh')
ax2.autoscale('tight')

plt.show()
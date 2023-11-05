import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 3))
fig.subplots_adjust(wspace=0.35, left=0.09, right=0.95)

x = np.linspace(0.9, 1.7, 10)
y = 10 ** x[np.random.randint(0, 10, 10)]

ax2.semilogy(x, y)
ax2.set_title('v2.0')

with plt.style.context('classic'):
    ax1.semilogy(x, y)
    ax1.set_xlim(ax2.get_xlim())
    ax1.set_ylim(ax2.get_ylim())
    ax1.set_title('classic')
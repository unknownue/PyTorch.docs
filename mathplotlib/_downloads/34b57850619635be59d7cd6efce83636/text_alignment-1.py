import matplotlib.pyplot as plt
import numpy as np

y = [0.22, 0.34, 0.5, 0.56, 0.78]
x = [0.17, 0.5, 0.855]
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
ax.set(xlim=(0, 1), ylim=(0, 1), xticks=[], yticks=[])
ax.spines[:].set_visible(False)
ax.text(0.5, 0.5, 'plot', fontsize=128, ha='center', va='center', zorder=1)
ax.hlines(y, x[0], x[-1], color='grey')
ax.vlines(x, y[0], y[-1], color='grey')
ax.plot(X.ravel(), Y.ravel(), 'o')
pad_x = 0.02
pad_y = 0.04
ax.text(x[0] - pad_x, y[0], 'bottom', ha='right', va='center')
ax.text(x[0] - pad_x, y[1], 'baseline', ha='right', va='center')
ax.text(x[0] - pad_x, y[2], 'center', ha='right', va='center')
ax.text(x[0] - pad_x, y[3], 'center_baseline', ha='right', va='center')
ax.text(x[0] - pad_x, y[4], 'top', ha='right', va='center')
ax.text(x[0], y[0] - pad_y, 'left', ha='center', va='top')
ax.text(x[1], y[0] - pad_y, 'center', ha='center', va='top')
ax.text(x[2], y[0] - pad_y, 'right', ha='center', va='top')
ax.set_xlabel('horizontalalignment', fontsize=14)
ax.set_ylabel('verticalalignment', fontsize=14, labelpad=35)
ax.set_title(
    'Relative position of text anchor point depending on alignment')
plt.show()
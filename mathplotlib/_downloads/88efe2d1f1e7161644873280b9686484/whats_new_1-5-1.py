import numpy as np
from cycler import cycler
cmap = cycler('cmap', ['viridis', 'magma','plasma', 'inferno'])
x_mode = cycler('x', [1, 2])
y_mode = cycler('y', x_mode)

cy = (x_mode * y_mode) + cmap

def demo(ax, x, y, cmap):
    X, Y = np.ogrid[0:2*np.pi:200j, 0:2*np.pi:200j]
    data = np.sin(X*x) * np.cos(Y*y)
    ax.imshow(data, interpolation='none', cmap=cmap)
    ax.set_title(cmap)

fig, axes = plt.subplots(2, 2)
for ax, sty in zip(axes.ravel(), cy):
    demo(ax, **sty)

fig.tight_layout()
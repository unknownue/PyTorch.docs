import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': '3d'},
                       constrained_layout=True)

x, y = np.mgrid[1:10:1, 1:10:1]
z = x ** 3 + y ** 3 - 500
z = np.ma.masked_array(z, z < 0)

ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0, cmap='inferno')
ax.view_init(35, -90)
import matplotlib.pyplot as plt
import numpy as np

# prepare some coordinates
x, y, z = np.indices((8, 8, 8))

# draw cuboids in the top left and bottom right corners, and a link between them
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

# combine the objects into a single boolean array
voxels = cube1 | cube2 | link

# set the colors of each object
colors = np.empty(voxels.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'

# and plot everything
fig = plt.figure(figsize=plt.figaspect(0.5))
ax, ax_shaded = fig.subplots(1, 2, subplot_kw=dict(projection='3d'))
ax.voxels(voxels, facecolors=colors, edgecolor='k', shade=False)
ax.set_title("Unshaded")
ax_shaded.voxels(voxels, facecolors=colors, edgecolor='k', shade=True)
ax_shaded.set_title("Shaded (default)")

plt.show()
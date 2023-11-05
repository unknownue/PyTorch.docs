import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define 3D shape
block = np.array([
    [[1, 1, 0],
     [1, 0, 0],
     [0, 1, 0]],
    [[1, 1, 0],
     [1, 1, 1],
     [1, 0, 0]],
    [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 0]],
    [[1, 0, 0],
     [1, 1, 1],
     [0, 1, 0]]
])

ax = plt.subplot(projection='3d')
pc = Poly3DCollection(block, facecolors='b', shade=True)
ax.add_collection(pc)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

colors = np.linspace(0, 1, 90).reshape((5, 6, 3))
plt.pcolormesh(colors)
plt.show()
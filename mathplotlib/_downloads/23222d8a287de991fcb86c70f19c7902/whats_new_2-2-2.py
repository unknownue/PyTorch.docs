import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
pcm = ax.pcolormesh(np.random.rand(32,32), cmap='cividis')
fig.colorbar(pcm)
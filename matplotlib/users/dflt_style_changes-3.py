import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))

ax1.grid(color='k', linewidth=.5, linestyle=':')
ax1.set_title('classic')

ax2.grid()
ax2.set_title('v2.0')
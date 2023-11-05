import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoLocator

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(4, 3), tight_layout=True)
ax1.set_xlim(0, .1)
ax2.set_xlim(0, .1)

ax1.xaxis.get_major_locator().set_params(nbins=9, steps=[1, 2, 5, 10])
ax1.set_title('classic')
ax2.set_title('v2.0')
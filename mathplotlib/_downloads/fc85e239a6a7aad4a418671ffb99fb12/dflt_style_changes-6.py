import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

# example variable error bar values
yerr = 0.1 + 0.2*np.sqrt(x)
xerr = 0.1 + yerr

def demo(ax, rc, title):
    with mpl.rc_context(rc=rc):
        ax.errorbar(x, y, xerr=0.2, yerr=0.4)
    ax.set_title(title)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3), tight_layout=True)

demo(ax1, {'errorbar.capsize': 3}, 'classic')
demo(ax2, {}, 'v2.0')
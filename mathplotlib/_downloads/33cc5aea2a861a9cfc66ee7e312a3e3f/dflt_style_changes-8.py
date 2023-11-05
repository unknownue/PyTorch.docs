import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))
fig.subplots_adjust(wspace=0.3)
th = np.linspace(0, 2*np.pi, 128)
N = 5

def demo(ax, extra_kwargs, title):
    ax.set_title(title)
    return [ax.fill_between(th, np.sin((j / N) * np.pi + th), alpha=.5, **extra_kwargs)
            for j in range(N)]

demo(ax1, {'facecolor': 'C0'}, 'classic')
demo(ax2, {}, 'v2.0')
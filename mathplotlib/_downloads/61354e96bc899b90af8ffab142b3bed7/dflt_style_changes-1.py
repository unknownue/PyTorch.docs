import numpy as np
import matplotlib.pyplot as plt

th = np.linspace(0, 2*np.pi, 512)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))


def color_demo(ax, colors, title):
    ax.set_title(title)
    for j, c in enumerate(colors):
        v_offset = -(j / len(colors))
        ax.plot(th, .1*np.sin(th) + v_offset, color=c)
        ax.annotate("'C{}'".format(j), (0, v_offset),
                    xytext=(-1.5, 0),
                    ha='right',
                    va='center',
                    color=c,
                    textcoords='offset points',
                    family='monospace')

        ax.annotate("{!r}".format(c), (2*np.pi, v_offset),
                    xytext=(1.5, 0),
                    ha='left',
                    va='center',
                    color=c,
                    textcoords='offset points',
                    family='monospace')
    ax.axis('off')

old_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']

color_demo(ax1, old_colors, 'classic')
color_demo(ax2, new_colors, 'v2.0')

fig.subplots_adjust(**{'bottom': 0.0, 'left': 0.059,
                       'right': 0.869, 'top': 0.895})
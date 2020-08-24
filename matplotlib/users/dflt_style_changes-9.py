import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc_context
import matplotlib.patches as mpatches

fig, all_ax = plt.subplots(3, 2, figsize=(4, 6), tight_layout=True)

def demo(ax_top, ax_mid, ax_bottom, rcparams, label):
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    fracs = [15, 30, 45, 10]

    explode = (0, 0.05, 0, 0)

    ax_top.set_title(label)

    with rc_context(rc=rcparams):
        ax_top.pie(fracs, labels=labels)
        ax_top.set_aspect('equal')
        ax_mid.bar(range(len(fracs)), fracs, tick_label=labels)
        plt.setp(ax_mid.get_xticklabels(), rotation=-45)
        grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T

        ax_bottom.set_xlim(0, .75)
        ax_bottom.set_ylim(0, .75)
        ax_bottom.add_artist(mpatches.Rectangle(grid[1] - [0.025, 0.05],
                                                0.05, 0.1))
        ax_bottom.add_artist(mpatches.RegularPolygon(grid[3], 5, 0.1))
        ax_bottom.add_artist(mpatches.Ellipse(grid[4], 0.2, 0.1))
        ax_bottom.add_artist(mpatches.Circle(grid[0], 0.1))
        ax_bottom.axis('off')

demo(*all_ax[:, 0], rcparams={'patch.force_edgecolor': True,
                              'patch.facecolor': 'b'}, label='classic')
demo(*all_ax[:, 1], rcparams={}, label='v2.0')
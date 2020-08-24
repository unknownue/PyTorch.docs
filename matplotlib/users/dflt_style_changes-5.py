import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))

N = 15

x = np.arange(N)
y = np.ones_like(x)

sty_cycle = (cycler('ls', ['--' ,':', '-.']) *
             cycler('lw', [None, 1, 2, 5]))

classic = {
    'lines.linewidth': 1.0,
    'lines.dashed_pattern' : [6, 6],
    'lines.dashdot_pattern' : [3, 5, 1, 5],
    'lines.dotted_pattern' : [1, 3],
    'lines.scale_dashes': False}

v2 = {}
#    {'lines.linewidth': 1.5,
#     'lines.dashed_pattern' : [2.8, 1.2],
#     'lines.dashdot_pattern' : [4.8, 1.2, 0.8, 1.2],
#     'lines.dotted_pattern' : [1.1, 1.1],
#     'lines.scale_dashes': True}

def demo(ax, rcparams, title):
    ax.axis('off')
    ax.set_title(title)
    with mpl.rc_context(rc=rcparams):
        for j, sty in enumerate(sty_cycle):
            ax.plot(x, y + j, **sty)

demo(ax1, classic, 'classic')
demo(ax2, {}, 'v2.0')
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def demo(ax, rcparams, title):
    np.random.seed(2)
    N = 25
    with mpl.rc_context(rc=rcparams):
        x = range(N)
        y = np.cumsum(np.random.randn(N) )
        # unpack the single Line2D artist
        ln, = ax.plot(x, y, marker='s',
                      linestyle='-', label='plot')
        ax.fill_between(x, y, 0, label='fill', alpha=.5, color=ln.get_color())
        ax.scatter(N*np.random.rand(N), np.random.rand(N), label='scatter')
        ax.set_title(title)
        ax.legend()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3), tight_layout=True)

classic_rc = {'legend.fancybox': False,
              'legend.numpoints': 2,
              'legend.scatterpoints': 3,
              'legend.framealpha': None,
              'legend.edgecolor': 'inherit',
              'legend.loc': 'upper right',
              'legend.fontsize': 'large'}

demo(ax1, classic_rc, 'classic')
demo(ax2, {}, 'v2.0')
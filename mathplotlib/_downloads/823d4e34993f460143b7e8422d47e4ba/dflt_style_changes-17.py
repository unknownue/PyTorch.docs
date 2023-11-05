import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

th = np.linspace(0, 2*np.pi, 128)
y = np.sin(th)

def demo(fig, rcparams, title, j):
    np.random.seed(2)
    with mpl.rc_context(rc=rcparams):

        ax = fig.add_subplot(2, 2, j)
        ax.hist(np.random.beta(0.5, 0.5, 10000), 25, density=True)
        ax.set_xlim([0, 1])
        ax.set_title(title)

        ax = fig.add_subplot(2, 2, j + 2)
        ax.imshow(np.random.rand(5, 5))

classic = {'xtick.direction': 'in',
           'ytick.direction': 'in',
           'xtick.top': True,
           'ytick.right': True}

fig = plt.figure(figsize=(6, 6), tight_layout=True)

demo(fig, classic, 'classic', 1)
demo(fig, {}, 'v2.0', 2)
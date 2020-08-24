import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def demo(ax, rcparams, title):
    np.random.seed(2)
    A = np.random.rand(5, 5)

    with mpl.rc_context(rc=rcparams):
        ax.imshow(A)
        ax.set_title(title)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3), tight_layout=True)

classic_rcparams = {'image.interpolation': 'bilinear',
                    'image.resample': False}

demo(ax1, classic_rcparams, 'classic')
demo(ax2, {}, 'v2.0')
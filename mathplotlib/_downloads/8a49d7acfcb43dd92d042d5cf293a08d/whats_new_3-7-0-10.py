import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng(19680801)
imdata = rng.random((10, 10))
fig, ax = plt.subplots(layout='constrained')
im = ax.imshow(imdata)
fig.colorbar(im, cax=ax.inset_axes([0, 1.05, 1, 0.05]),
             location='top')
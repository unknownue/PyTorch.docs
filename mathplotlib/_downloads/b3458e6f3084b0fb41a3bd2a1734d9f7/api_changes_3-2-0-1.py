import matplotlib.pyplot as plt
import numpy as np

fig, (ax_old, ax_new) = plt.subplots(1, 2, constrained_layout=True)

ax_new.set_title('new values (-5, 6)')
ax_old.set_title('old values (-7, 7)')

x = np.logspace(-8, 8, 1024)
y = 1e-5 * np.exp(-x / 1e5) + 1e-6

ax_old.xaxis.get_major_formatter().set_powerlimits((-7, 7))
ax_old.yaxis.get_major_formatter().set_powerlimits((-7, 7))

for ax in [ax_new, ax_old]:
    ax.plot(x, y)
    ax.set_xlim(0, 1e6)
    ax.set_ylim(1e-6, 1e-5)
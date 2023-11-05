options = ['left', 'center', 'right']
fig, axs = plt.subplots(len(options), 1, constrained_layout=True)
for ax, loc in zip(axs, options):
    ax.plot([1, 2, 3])
    ax.set_xlabel(f'xlabel loc={loc!r}', loc=loc)

options = ['bottom', 'center', 'top']
fig, axs = plt.subplots(1, len(options), constrained_layout=True)
for ax, loc in zip(axs, options):
    ax.plot([1, 2, 3])
    ax.set_ylabel(f'ylabel loc={loc!r}', loc=loc)
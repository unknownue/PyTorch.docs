fig, axs = plt.subplots(1, 2)

for i, ax in enumerate(axs):
    ax.axline((0.25, 0), slope=2, transform=ax.transAxes)
    ax.set(xlim=(i, i+5), ylim=(i, i+5))
fig, axs = plt.subplots(1, 3)
for i, ax in enumerate(axs):
    ax.plot([1, 2, 3])
    ax.set_title(f'Axes {i}')

fig.suptitle('suptitle')
fig.tight_layout()
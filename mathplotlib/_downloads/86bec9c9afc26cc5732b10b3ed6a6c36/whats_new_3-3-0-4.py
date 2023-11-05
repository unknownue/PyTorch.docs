fig, axs = plt.subplots(1, 3)
for i, ax in enumerate(axs):
    ax.plot([1, 2, 3])
    ax.set_title(f'Axes {i}')

t = fig.suptitle('suptitle')
t.set_in_layout(False)
fig.tight_layout()
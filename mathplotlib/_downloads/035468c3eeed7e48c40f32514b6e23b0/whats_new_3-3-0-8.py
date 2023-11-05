options = ['C3', 'linecolor', 'markerfacecolor', 'markeredgecolor']

fig, axs = plt.subplots(2, 2, constrained_layout=True)
for ax, color in zip(axs.flat, options):
    ax.plot([1, 2, 3], marker='o',
            color='C0', markerfacecolor='C1', markeredgecolor='C2',
            linewidth=3, markersize=10, markeredgewidth=3,
            label='a line')

    ax.legend(labelcolor=color)
    ax.set_title(f'labelcolor={color!r}')

    ax.margins(0.1)
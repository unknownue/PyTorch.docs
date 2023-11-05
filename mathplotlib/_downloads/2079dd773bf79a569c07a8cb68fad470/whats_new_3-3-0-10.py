from matplotlib import ticker

titles = ["'{x} km'", "lambda x, pos: str(x-5)"]
formatters = ['{x} km', lambda x, pos: str(x-5)]

fig, axs = plt.subplots(2, 1, figsize=(8, 2), constrained_layout=True)

for ax, title, formatter in zip(axs, titles, formatters):
    # only show the bottom spine
    ax.yaxis.set_major_locator(ticker.NullLocator())
    for spine in ['top', 'left', 'right']:
        ax.spines[spine].set_visible(False)

    # define tick positions
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, f'ax.xaxis.set_major_formatter({title})',
            transform=ax.transAxes, fontsize=14, fontname='Monospace',
            color='tab:blue')

    ax.xaxis.set_major_formatter(formatter)
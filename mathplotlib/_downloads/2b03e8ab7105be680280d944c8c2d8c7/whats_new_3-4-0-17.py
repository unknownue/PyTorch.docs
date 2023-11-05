np.random.seed(19680801)
fig, axs = plt.subplots(3, 2, figsize=(5, 5), constrained_layout=True,
                        sharex=True, sharey=True)

for nn, ax in enumerate(axs.flat):
    ax.set_title(f'Channel {nn}')
    ax.plot(np.cumsum(np.random.randn(50)))

fig.supxlabel('Time [s]')
fig.supylabel('Data [V]')
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(5, 3), tight_layout=True)
gs = gridspec.GridSpec(2, 2)

ax = fig.add_subplot(gs[0,:])
ax.plot(np.arange(0, 1e6, 1000))
ax.set_ylabel('Test')
for i in range(2):
    ax = fig.add_subplot(gs[1, i])
    ax.set_ylabel('Booooo')
    ax.set_xlabel('Hello')
    if i == 0:
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)
fig.align_labels()
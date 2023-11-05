x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4,
            linestyle=':', color='darkgrey',
            marker='o', markersize=20, fillstyle='left',
            markerfacecolor='tab:blue', markerfacecoloralt='tab:orange',
            markeredgecolor='tab:brown', markeredgewidth=2)
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
offsets = [0, 1]

plt.rcParams['axes.prop_cycle'] = plt.cycler('linestyle', ['-', '--'])

fig, ax = plt.subplots()
for offset in offsets:
    ax.errorbar(x, y + offset, xerr=0.1, yerr=0.3, fmt='tab:blue')
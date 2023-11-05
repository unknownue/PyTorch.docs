locs = np.linspace(0.1, 2 * np.pi, 25)
heads = np.cos(locs)

fig, ax = plt.subplots()
ax.stem(locs, heads, orientation='horizontal')
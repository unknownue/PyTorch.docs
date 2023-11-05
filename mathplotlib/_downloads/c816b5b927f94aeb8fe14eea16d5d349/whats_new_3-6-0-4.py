fig, ax = plt.subplots()

ax.plot([0, 2], [1, 2])

polar_ax = ax.inset_axes([0.75, 0.25, 0.2, 0.2], projection='polar')
polar_ax.plot([0, 2], [1, 2])
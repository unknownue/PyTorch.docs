fig, ax = plt.subplots()

ax.axline((.1, .1), slope=5, color='C0', label='by slope')
ax.axline((.1, .2), (.8, .7), color='C3', label='by points')

ax.legend()
import matplotlib.patches as mpatches

fig, ax = plt.subplots()
ax.set(xlim=(0, 1), ylim=(-1, 4))

for i, stylename in enumerate((']-[', '|-|')):
    for j, angle in enumerate([-30, 60]):
        arrowstyle = f'{stylename},angleA={angle},angleB={-angle}'
        patch = mpatches.FancyArrowPatch((0.1, 2*i + j), (0.9, 2*i + j),
                                         arrowstyle=arrowstyle,
                                         mutation_scale=25)
        ax.text(0.5, 2*i + j, arrowstyle,
                verticalalignment='bottom', horizontalalignment='center')
        ax.add_patch(patch)
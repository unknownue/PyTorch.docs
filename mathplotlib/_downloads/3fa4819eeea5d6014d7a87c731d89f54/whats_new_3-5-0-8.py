import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import art3d

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4, 3),
                               subplot_kw=dict(projection='3d'))

ax1.set_title('computed_zorder = True (default)')
ax2.set_title('computed_zorder = False')
ax2.computed_zorder = False

corners = ((0, 0, 0), (0, 5, 0), (5, 5, 0), (5, 0, 0))
for ax in (ax1, ax2):
    tri = art3d.Poly3DCollection([corners],
                                 facecolors='white',
                                 edgecolors='black',
                                 zorder=1)
    ax.add_collection3d(tri)
    line, = ax.plot((2, 2), (2, 2), (0, 4), c='red', zorder=2,
                    label='zorder=2')
    points = ax.scatter((3, 3), (1, 3), (1, 3), c='red', zorder=10,
                        label='zorder=10')

    ax.set_xlim((0, 5))
    ax.set_ylim((0, 5))
    ax.set_zlim((0, 2.5))

plane = mpatches.Patch(facecolor='white', edgecolor='black',
                       label='zorder=1')
fig.legend(handles=[plane, line, points], loc='lower center')
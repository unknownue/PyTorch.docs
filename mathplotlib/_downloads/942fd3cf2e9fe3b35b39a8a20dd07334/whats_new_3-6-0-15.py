from matplotlib.markers import CapStyle, JoinStyle, MarkerStyle
from matplotlib.transforms import Affine2D

fig, axs = plt.subplots(3, 1, layout='constrained')
for ax in axs:
    ax.axis('off')
    ax.set_xlim(-0.5, 2.5)

axs[0].set_title('Cap styles', fontsize=14)
for col, cap in enumerate(CapStyle):
    axs[0].plot(col, 0, markersize=32, markeredgewidth=8,
                marker=MarkerStyle('1', capstyle=cap))
    # Show the marker edge for comparison with the cap.
    axs[0].plot(col, 0, markersize=32, markeredgewidth=1,
                markerfacecolor='none', markeredgecolor='lightgrey',
                marker=MarkerStyle('1'))
    axs[0].annotate(cap.name, (col, 0),
                    xytext=(20, -5), textcoords='offset points')

axs[1].set_title('Join styles', fontsize=14)
for col, join in enumerate(JoinStyle):
    axs[1].plot(col, 0, markersize=32, markeredgewidth=8,
                marker=MarkerStyle('*', joinstyle=join))
    # Show the marker edge for comparison with the join.
    axs[1].plot(col, 0, markersize=32, markeredgewidth=1,
                markerfacecolor='none', markeredgecolor='lightgrey',
                marker=MarkerStyle('*'))
    axs[1].annotate(join.name, (col, 0),
                    xytext=(20, -5), textcoords='offset points')

axs[2].set_title('Arbitrary transforms', fontsize=14)
for col, (size, rot) in enumerate(zip([2, 5, 7], [0, 45, 90])):
    t = Affine2D().rotate_deg(rot).scale(size)
    axs[2].plot(col, 0, marker=MarkerStyle('*', transform=t))
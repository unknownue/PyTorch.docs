fig, ax = plt.subplots()

rect = plt.Rectangle((0, 0), 1, 1, facecolor='none', edgecolor='C0')
ax.add_patch(rect)
ax.annotate('Unrotated', (1, 0), color='C0',
            horizontalalignment='right', verticalalignment='top',
            xytext=(0, -3), textcoords='offset points')

for rotation_point, color in zip(['xy', 'center', (0.75, 0.25)],
                                 ['C1', 'C2', 'C3']):
    ax.add_patch(
        plt.Rectangle((0, 0), 1, 1, facecolor='none', edgecolor=color,
                      angle=45, rotation_point=rotation_point))

    if rotation_point == 'center':
        point = 0.5, 0.5
    elif rotation_point == 'xy':
        point = 0, 0
    else:
        point = rotation_point
    ax.plot(point[:1], point[1:], color=color, marker='o')

    label = f'{rotation_point}'
    if label == 'xy':
        label += ' (default)'
    ax.annotate(label, point, color=color,
                xytext=(3, 3), textcoords='offset points')

ax.set_aspect(1)
ax.set_title('rotation_point options')
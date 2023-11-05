from itertools import combinations, product

aspects = [
    ['auto', 'equal', '.'],
    ['equalxy', 'equalyz', 'equalxz'],
]
fig, axs = plt.subplot_mosaic(aspects, figsize=(7, 6),
                              subplot_kw={'projection': '3d'})

# Draw rectangular cuboid with side lengths [1, 1, 5]
r = [0, 1]
scale = np.array([1, 1, 5])
pts = combinations(np.array(list(product(r, r, r))), 2)
for start, end in pts:
    if np.sum(np.abs(start - end)) == r[1] - r[0]:
        for ax in axs.values():
            ax.plot3D(*zip(start*scale, end*scale), color='C0')

# Set the aspect ratios
for aspect, ax in axs.items():
    ax.set_box_aspect((3, 4, 5))
    ax.set_aspect(aspect)
    ax.set_title(f'set_aspect({aspect!r})')
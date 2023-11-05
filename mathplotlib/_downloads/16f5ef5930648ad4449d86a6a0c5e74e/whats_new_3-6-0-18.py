from mpl_toolkits.mplot3d import axes3d

X, Y, Z = axes3d.get_test_data(0.05)

fig, axs = plt.subplots(1, 3, figsize=(7, 4),
                        subplot_kw={'projection': '3d'})

for ax, focal_length in zip(axs, [0.2, 1, np.inf]):
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    ax.set_proj_type('persp', focal_length=focal_length)
    ax.set_title(f"{focal_length=}")
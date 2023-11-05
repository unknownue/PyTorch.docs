theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
directions = ['z', 'x', 'y']
names = [r'$\theta$', r'$\cos\theta$', r'$\sin\theta$']

fig, axs = plt.subplots(1, 3, figsize=(8, 4),
                        constrained_layout=True,
                        subplot_kw={'projection': '3d'})
for ax, zdir, name in zip(axs, directions, names):
    ax.stem(x, y, z, orientation=zdir)
    ax.set_title(name)
fig.suptitle(r'A parametric circle: $(x, y) = (\cos\theta, \sin\theta)$')
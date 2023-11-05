Nphi, Nr = 18, 8
phi = np.linspace(0, np.pi, Nphi)
r = np.arange(Nr)
phi = np.tile(phi, Nr).flatten()
r = np.repeat(r, Nphi).flatten()

x = r * np.sin(phi)
y = r * np.cos(phi)
z = Nr - r

fig, axs = plt.subplots(1, 3, figsize=(7, 3),
                        subplot_kw=dict(projection='3d'),
                        gridspec_kw=dict(wspace=0.4, left=0.08, right=0.98,
                                         bottom=0, top=1))
for vert_a, ax in zip(['z', 'y', 'x'], axs):
    pc = ax.scatter(x, y, z, c=z)
    ax.view_init(azim=30, elev=30, vertical_axis=vert_a)
    ax.set(xlabel='x', ylabel='y', zlabel='z',
           title=f'vertical_axis={vert_a!r}')
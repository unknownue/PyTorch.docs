x = np.arange(5, dtype=float)
y = np.arange(5, dtype=float)
# z and zalpha for demo pcolormesh
z = x[1:, np.newaxis] + y[np.newaxis, 1:]
zalpha = np.ones_like(z)
zalpha[::2, ::2] = 0.3  # alternate patches are partly transparent
# s and salpha for demo scatter
s = x
salpha = np.linspace(0.1, 0.9, len(x))  # just a ramp

fig, axs = plt.subplots(2, 2, constrained_layout=True)
axs[0, 0].pcolormesh(x, y, z, alpha=zalpha)
axs[0, 0].set_title("pcolormesh")
axs[0, 1].scatter(x, y, c=s, alpha=salpha)
axs[0, 1].set_title("color-mapped")
axs[1, 0].scatter(x, y, c='k', alpha=salpha)
axs[1, 0].set_title("c='k'")
axs[1, 1].scatter(x, y, c=['r', 'g', 'b', 'c', 'm'], alpha=salpha)
axs[1, 1].set_title("c=['r', 'g', 'b', 'c', 'm']")
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
cmaps = ['turbo', 'jet', 'gist_rainbow_r', 'hsv_r']

fig, axs = plt.subplots(len(cmaps), constrained_layout=True)
for name, ax in zip(cmaps, axs):
    ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
    ax.set_title(name)
    ax.set_axis_off()
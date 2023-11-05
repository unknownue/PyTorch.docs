delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

fig, axs = plt.subplots(1, 2)

CS = axs[0].contour(X, Y, Z, 6, colors='k')
axs[0].clabel(CS, fontsize=9, inline=True)
axs[0].set_title('Default negative contours')

CS = axs[1].contour(X, Y, Z, 6, colors='k', negative_linestyles='dotted')
axs[1].clabel(CS, fontsize=9, inline=True)
axs[1].set_title('Dotted negative contours')
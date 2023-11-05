fig, (ax0, ax1) = plt.subplots(1, 2, sharex=True)
x = np.linspace(-3, 6, 100)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title(r'$sinh^{-1}$')

for p in (-2, 2):
    for ax in (ax0, ax1):
        c = plt.Circle((p, p), radius=0.5, fill=False,
                       color='red', alpha=0.8, lw=3)
        ax.add_patch(c)
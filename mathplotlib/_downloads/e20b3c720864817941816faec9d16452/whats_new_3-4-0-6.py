x = np.linspace(0, 1, 15)
y = x * (1-x)
yerr = y/6

fig, ax = plt.subplots(2, constrained_layout=True)
ax[0].errorbar(x, y, yerr, capsize=2)
ax[0].set_title('errorevery unspecified')

ax[1].errorbar(x, y, yerr, capsize=2,
               errorevery=[False, True, True, False, True] * 3)
ax[1].set_title('errorevery=[False, True, True, False, True] * 3')
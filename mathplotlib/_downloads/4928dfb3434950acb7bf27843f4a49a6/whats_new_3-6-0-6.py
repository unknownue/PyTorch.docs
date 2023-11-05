x = np.linspace(-7, 7, 140)
x = np.hstack([-25, x, 25])
capwidths = [0.01, 0.2]

fig, ax = plt.subplots()
ax.boxplot([x, x], notch=True, capwidths=capwidths)
ax.set_title(f'{capwidths=}')
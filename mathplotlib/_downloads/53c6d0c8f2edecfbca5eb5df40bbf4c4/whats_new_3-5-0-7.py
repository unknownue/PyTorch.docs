plt.rcParams['legend.labelcolor'] = 'linecolor'

# Make some fake data.
a = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]

fig, ax = plt.subplots()
ax.plot(a, c, 'g--', label='Model length')
ax.plot(a, d, 'r:', label='Data length')

ax.legend()

plt.show()
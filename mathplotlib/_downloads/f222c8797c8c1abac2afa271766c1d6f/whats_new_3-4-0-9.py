np.random.seed(0)
h, edges = np.histogram(np.random.normal(5, 2, 5000),
                        bins=np.linspace(0,10,20))

fig, ax = plt.subplots(constrained_layout=True)

ax.stairs(h, edges)

plt.show()
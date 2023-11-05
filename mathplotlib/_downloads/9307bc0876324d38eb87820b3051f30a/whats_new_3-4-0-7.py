data = {
    'a': np.random.rand(1000),
    'b': np.random.rand(1000),
    'c': np.random.rand(1000),
}

fig, ax = plt.subplots()
ax.hexbin('a', 'b', C='c', data=data, gridsize=10)
from matplotlib.colors import CenteredNorm

np.random.seed(20201004)
data = np.random.normal(size=(3, 4), loc=1)

fig, ax = plt.subplots()
pc = ax.pcolormesh(data, cmap=plt.get_cmap('RdGy'), norm=CenteredNorm())
fig.colorbar(pc)
ax.set_title('data centered around zero')

# add text annotation
for irow, data_row in enumerate(data):
    for icol, val in enumerate(data_row):
        ax.text(icol + 0.5, irow + 0.5, f'{val:.2f}', color='C0',
                size=16, va='center', ha='center')
plt.show()
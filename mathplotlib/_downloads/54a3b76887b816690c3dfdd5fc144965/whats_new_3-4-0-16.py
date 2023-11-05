from matplotlib.colors import FuncNorm

def forward(x):
    return x**2
def inverse(x):
    return np.sqrt(x)

norm = FuncNorm((forward, inverse), vmin=0, vmax=3)

np.random.seed(20201004)
data = np.random.normal(size=(3, 4), loc=1)

fig, ax = plt.subplots()
pc = ax.pcolormesh(data, norm=norm)
fig.colorbar(pc)
ax.set_title('squared normalization')

# add text annotation
for irow, data_row in enumerate(data):
    for icol, val in enumerate(data_row):
        ax.text(icol + 0.5, irow + 0.5, f'{val:.2f}', color='C0',
                size=16, va='center', ha='center')
plt.show()
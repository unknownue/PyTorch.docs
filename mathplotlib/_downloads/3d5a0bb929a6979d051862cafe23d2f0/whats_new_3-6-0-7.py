x = ["a", "b", "c"]
y = [10, 20, 15]
color = ['C0', 'C1', 'C2']

fig, ax = plt.subplots()
ax.bar(x, y, color=color, label=x)
ax.legend()
fig, (ax1, ax2) = plt.subplots(ncols=2)
x = [10, 30, 60]

ax1.pie(x, hatch=['.', 'o', 'O'])
ax2.pie(x, hatch='.O')

ax1.set_title("hatch=['.', 'o', 'O']")
ax2.set_title("hatch='.O'")
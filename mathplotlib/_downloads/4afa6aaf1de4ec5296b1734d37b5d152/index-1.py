fig = plt.figure(figsize=(4, 2), facecolor='lightskyblue',
                 layout='constrained')
fig.suptitle('A nice Matplotlib Figure')
ax = fig.add_subplot()
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
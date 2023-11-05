import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(4, 4))

ax.plot([0.75, 0.75], [0.25, 0.75], 'ok')
ax.set(xlim=(0, 1), ylim=(0, 1), title='New ArrowStyle options')

ax.annotate(']->', (0.75, 0.25), (0.25, 0.25),
            arrowprops=dict(
                arrowstyle=']->', connectionstyle="arc3,rad=-0.05",
                shrinkA=5, shrinkB=5,
            ),
            bbox=dict(boxstyle='square', fc='w'), size='large')

ax.annotate('<-[', (0.75, 0.75), (0.25, 0.75),
            arrowprops=dict(
                arrowstyle='<-[', connectionstyle="arc3,rad=-0.05",
                shrinkA=5, shrinkB=5,
            ),
            bbox=dict(boxstyle='square', fc='w'), size='large')
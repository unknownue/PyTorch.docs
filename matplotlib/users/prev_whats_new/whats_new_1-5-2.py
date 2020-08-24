fig, ax = plt.subplots()
fig.patch.set_color('.9')
ax.text(.5, .75,
        "This is a really long string that should be wrapped so that "
        "it does not go outside the figure.", wrap=True)
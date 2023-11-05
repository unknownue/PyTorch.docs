from matplotlib.offsetbox import AnchoredText

fig, ax = plt.subplots()

text0 = AnchoredText("test\ntest long text", loc="center left",
                     pad=0.2, prop={"ha": "left"})
ax.add_artist(text0)

text1 = AnchoredText("test\ntest long text", loc="center",
                     pad=0.2, prop={"ha": "center"})
ax.add_artist(text1)

text2 = AnchoredText("test\ntest long text", loc="center right",
                     pad=0.2, prop={"ha": "right"})
ax.add_artist(text2)
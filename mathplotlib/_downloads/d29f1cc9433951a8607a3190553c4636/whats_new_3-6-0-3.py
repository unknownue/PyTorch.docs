fig, axs = plt.subplots(2, 2, figsize=(5, 3),
                        sharex=True, sharey=True, layout='compressed')
for ax in axs.flat:
    ax.imshow([[0, 1], [2, 3]])
fig.suptitle("fixed-aspect plots, layout='compressed'")
plt.style.use('classic')

plt.rcParams['savefig.facecolor'] = "0.8"
plt.rcParams['figure.figsize'] = 4, 3

fig, axes_list = plt.subplots(2, 1)
for ax in axes_list.flat:
    ax.set(xlabel="x-label", ylabel="y-label", title="before tight_layout")
ax.locator_params(nbins=3)

plt.show()

plt.rcParams['savefig.facecolor'] = "0.8"
plt.rcParams['figure.figsize'] = 4, 3

fig, axes_list = plt.subplots(2, 1)
for ax in axes_list.flat:
    ax.set(xlabel="x-label", ylabel="y-label", title="after tight_layout")
ax.locator_params(nbins=3)

plt.tight_layout()
plt.show()
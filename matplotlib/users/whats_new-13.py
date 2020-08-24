def label(x):
    return [str(v) for v in x]

x = np.array([0.25, 0.3, 0.3])
fig, ax = plt.subplots(2, 2, constrained_layout=True)

ax[0, 0].pie(x, autopct='%1.1f%%', labels=label(x), normalize=False)
ax[0, 0].set_title('normalize=False')
ax[0, 1].pie(x, autopct='%1.2f%%', labels=label(x), normalize=True)
ax[0, 1].set_title('normalize=True')

# This is supposed to show the 'old' behavior of not passing *normalize*
# explicitly, but for the purposes of keeping the documentation build
# warning-free, and future proof for when the deprecation is made
# permanent, we pass *normalize* here explicitly anyway.
ax[1, 0].pie(x, autopct='%1.2f%%', labels=label(x), normalize=False)
ax[1, 0].set_title('normalize unspecified\nsum(x) < 1')
ax[1, 1].pie(x * 10, autopct='%1.2f%%', labels=label(x * 10),
             normalize=True)
ax[1, 1].set_title('normalize unspecified\nsum(x) > 1')
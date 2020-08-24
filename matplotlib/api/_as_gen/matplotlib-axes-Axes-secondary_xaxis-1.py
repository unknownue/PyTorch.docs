fig, ax = plt.subplots()
ax.loglog(range(1, 360, 5), range(1, 360, 5))
ax.set_xlabel('frequency [Hz]')

def invert(x):
    return 1 / x

secax = ax.secondary_xaxis('top', functions=(invert, invert))
secax.set_xlabel('Period [s]')
plt.show()
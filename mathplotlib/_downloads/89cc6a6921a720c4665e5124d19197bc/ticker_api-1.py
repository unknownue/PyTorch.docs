lim = (1_000_000, 1_000_010)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, gridspec_kw={'hspace': 2})
ax1.set(title='offset_notation', xlim=lim)
ax2.set(title='scientific notation', xlim=lim)
ax2.xaxis.get_major_formatter().set_useOffset(False)
ax3.set(title='floating point notation', xlim=lim)
ax3.xaxis.get_major_formatter().set_useOffset(False)
ax3.xaxis.get_major_formatter().set_scientific(False)
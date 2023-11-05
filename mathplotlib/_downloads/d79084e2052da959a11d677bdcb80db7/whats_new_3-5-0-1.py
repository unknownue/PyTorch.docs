mosaic = [
    ['A', [['B', 'C'],
           ['D', 'E']]],
    ['F', 'G'],
]
fig = plt.figure(constrained_layout=True)
ax_dict = fig.subplot_mosaic(mosaic, sharex=True, sharey=True)
# All Axes use these scales after this call.
ax_dict['A'].set(xscale='log', yscale='logit')
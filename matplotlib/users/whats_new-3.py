np.random.seed(0)
x = np.random.random(100) * 100 + 20
y = np.random.random(100) * 50 + 25
c = np.random.random(100) - 0.5

fig = plt.figure(constrained_layout=True)
axd = fig.subplot_mosaic([['.', 'histx'], ['histy', 'scat']],
                         gridspec_kw={'width_ratios': [1, 7],
                                      'height_ratios': [2, 7]})

axd['histy'].invert_xaxis()
axd['histx'].sharex(axd['scat'])
axd['histy'].sharey(axd['scat'])

im = axd['scat'].scatter(x, y, c=c, cmap='RdBu', picker=True)
fig.colorbar(im, orientation='horizontal', ax=axd['scat'], shrink=0.8)

axd['histx'].hist(x)
axd['histy'].hist(y, orientation='horizontal')
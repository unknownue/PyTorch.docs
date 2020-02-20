from matplotlib.image import NonUniformImage
import matplotlib.pyplot as plt

# Construct a 2-D histogram with variable bin width. First define the bin
# edges:

xedges = [0, 1, 3, 5]
yedges = [0, 2, 3, 4, 6]

# Next we create a histogram H with random bin content:

x = np.random.normal(2, 1, 100)
y = np.random.normal(1, 1, 100)
H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
H = H.T  # Let each row list bins with common y range.

# :func:`imshow <matplotlib.pyplot.imshow>` can only display square bins:

fig = plt.figure(figsize=(7, 3))
ax = fig.add_subplot(131, title='imshow: square bins')
plt.imshow(H, interpolation='nearest', origin='low',
        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
# <matplotlib.image.AxesImage object at 0x...>

# :func:`pcolormesh <matplotlib.pyplot.pcolormesh>` can display actual edges:

ax = fig.add_subplot(132, title='pcolormesh: actual edges',
        aspect='equal')
X, Y = np.meshgrid(xedges, yedges)
ax.pcolormesh(X, Y, H)
# <matplotlib.collections.QuadMesh object at 0x...>

# :class:`NonUniformImage <matplotlib.image.NonUniformImage>` can be used to
# display actual bin edges with interpolation:

ax = fig.add_subplot(133, title='NonUniformImage: interpolated',
        aspect='equal', xlim=xedges[[0, -1]], ylim=yedges[[0, -1]])
im = NonUniformImage(ax, interpolation='bilinear')
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
im.set_data(xcenters, ycenters, H)
ax.images.append(im)
plt.show()

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)

fig, (ax0, ax1) = plt.subplots(1, 2, sharex=True)

ax0.streamplot(X, Y, U, V, broken_streamlines=True)
ax0.set_title('broken_streamlines=True')

ax1.streamplot(X, Y, U, V, broken_streamlines=False)
ax1.set_title('broken_streamlines=False')
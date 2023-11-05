from mpl_toolkits.mplot3d import axes3d

X, Y, Z = axes3d.get_test_data(0.05)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.view_init(elev=0, azim=0, roll=30)
ax.set_title('elev=0, azim=0, roll=30')
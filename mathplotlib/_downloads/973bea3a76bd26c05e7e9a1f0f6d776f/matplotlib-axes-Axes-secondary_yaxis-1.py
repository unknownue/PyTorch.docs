fig, ax = plt.subplots()
ax.plot(range(1, 360, 5), range(1, 360, 5))
ax.set_ylabel('degrees')
secax = ax.secondary_yaxis('right', functions=(np.deg2rad,
                                               np.rad2deg))
secax.set_ylabel('radians')
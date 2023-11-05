import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(range(360))
ax.secondary_xaxis('top', functions=(np.deg2rad, np.rad2deg))
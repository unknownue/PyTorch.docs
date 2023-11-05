from datetime import datetime, timedelta
from matplotlib.dates import ConciseDateFormatter

plt.rc('text', usetex=True)

t0 = datetime(1968, 8, 1)
ts = [t0 + i * timedelta(days=1) for i in range(10)]

fig, ax = plt.subplots()
ax.plot(ts, range(10))
ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))
ax.set_xlabel('Date')
ax.set_ylabel('Value')
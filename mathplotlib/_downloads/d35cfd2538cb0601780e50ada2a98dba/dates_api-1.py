import datetime
import matplotlib.dates as mdates

base = datetime.datetime(2005, 2, 1)
dates = np.array([base + datetime.timedelta(hours=(2 * i))
                  for i in range(732)])
N = len(dates)
np.random.seed(19680801)
y = np.cumsum(np.random.randn(N))

fig, ax = plt.subplots(constrained_layout=True)
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

ax.plot(dates, y)
ax.set_title('Concise Date Formatter')
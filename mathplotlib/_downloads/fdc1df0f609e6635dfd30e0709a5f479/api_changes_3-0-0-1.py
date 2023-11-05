import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

t0 = datetime.datetime(2009, 8, 20, 1, 10, 12)
tf = datetime.datetime(2009, 8, 20, 1, 42, 11)


fig, axs = plt.subplots(1, 2, constrained_layout=True)
ax = axs[0]
ax.axhspan(t0, tf, facecolor="blue", alpha=0.25)
ax.set_ylim(t0 - datetime.timedelta(minutes=3),
            tf + datetime.timedelta(minutes=3))
ax.set_title('NEW DEFAULT')

ax = axs[1]
ax.axhspan(t0, tf, facecolor="blue", alpha=0.25)
ax.set_ylim(t0 - datetime.timedelta(minutes=3),
            tf + datetime.timedelta(minutes=3))
# old behavior
locator = mdates.AutoDateLocator(interval_multiples=False, )
ax.yaxis.set_major_locator(locator)
ax.yaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

ax.set_title('OLD')
plt.show()
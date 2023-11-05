dates = np.arange('2001-01-10', '2001-05-23', dtype='datetime64[D]')
y = np.sin(dates.astype(float) / 10)
fig, axs = plt.subplots(nrows=2, constrained_layout=True)

plt.rcParams['date.converter'] = 'concise'
plt.rcParams['date.interval_multiples'] = True
axs[0].plot(dates, y)

plt.rcParams['date.converter'] = 'auto'
plt.rcParams['date.interval_multiples'] = False
axs[1].plot(dates, y)
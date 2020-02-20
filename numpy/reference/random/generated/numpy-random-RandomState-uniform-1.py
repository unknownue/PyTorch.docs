# Draw samples from the distribution:

s = np.random.uniform(-1,0,1000)

# All values are within the given interval:

np.all(s >= -1)
# True
np.all(s < 0)
# True

# Display the histogram of the samples, along with the
# probability density function:

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 15, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()

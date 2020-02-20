# Draw samples from the distribution:

shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
s = np.random.default_rng().gamma(shape, scale, 1000)

# Display the histogram of the samples, along with
# the probability density function:

import matplotlib.pyplot as plt
import scipy.special as sps  # doctest: +SKIP
count, bins, ignored = plt.hist(s, 50, density=True)
y = bins**(shape-1)*(np.exp(-bins/scale) /  # doctest: +SKIP
                     (sps.gamma(shape)*scale**shape))
plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
plt.show()

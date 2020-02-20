# Draw samples from the distribution:

mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

# Verify the mean and the variance:

abs(mu - np.mean(s))
# 0.0  # may vary

abs(sigma - np.std(s, ddof=1))
# 0.1  # may vary

# Display the histogram of the samples, along with
# the probability density function:

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()

# Two-by-four array of samples from N(3, 6.25):

np.random.normal(3, 2.5, size=(2, 4))
# array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
# [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random

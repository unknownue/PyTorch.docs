# Draw samples from the distribution:

mu, sigma = 3., 1. # mean and standard deviation
s = np.random.lognormal(mu, sigma, 1000)

# Display the histogram of the samples, along with
# the probability density function:

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 100, density=True, align='mid')

x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
       / (x * sigma * np.sqrt(2 * np.pi)))

plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')
plt.show()

# Demonstrate that taking the products of random samples from a uniform
# distribution can be fit well by a log-normal probability density
# function.

# Generate a thousand samples: each is the product of 100 random
# values, drawn from a normal distribution.
b = []
for i in range(1000):
   a = 10. + np.random.standard_normal(100)
   b.append(np.product(a))

b = np.array(b) / np.min(b) # scale values to be positive
count, bins, ignored = plt.hist(b, 100, density=True, align='mid')
sigma = np.std(np.log(b))
mu = np.mean(np.log(b))

x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
       / (x * sigma * np.sqrt(2 * np.pi)))

plt.plot(x, pdf, color='r', linewidth=2)
plt.show()

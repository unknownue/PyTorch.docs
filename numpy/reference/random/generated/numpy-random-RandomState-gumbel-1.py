# Draw samples from the distribution:

mu, beta = 0, 0.1 # location and scale
s = np.random.gumbel(mu, beta, 1000)

# Display the histogram of the samples, along with
# the probability density function:

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
         * np.exp( -np.exp( -(bins - mu) /beta) ),
         linewidth=2, color='r')
plt.show()

# Show how an extreme value distribution can arise from a Gaussian process
# and compare to a Gaussian:

means = []
maxima = []
for i in range(0,1000) :
   a = np.random.normal(mu, beta, 1000)
   means.append(a.mean())
   maxima.append(a.max())
count, bins, ignored = plt.hist(maxima, 30, density=True)
beta = np.std(maxima) * np.sqrt(6) / np.pi
mu = np.mean(maxima) - 0.57721*beta
plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
         * np.exp(-np.exp(-(bins - mu)/beta)),
         linewidth=2, color='r')
plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))
         * np.exp(-(bins - mu)**2 / (2 * beta**2)),
         linewidth=2, color='g')
plt.show()

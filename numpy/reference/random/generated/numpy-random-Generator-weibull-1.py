# Draw samples from the distribution:

rng = np.random.default_rng()
a = 5. # shape
s = rng.weibull(a, 1000)

# Display the histogram of the samples, along with
# the probability density function:

import matplotlib.pyplot as plt
x = np.arange(1,100.)/50.
def weib(x,n,a):
    return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)

count, bins, ignored = plt.hist(rng.weibull(5.,1000))
x = np.arange(1,100.)/50.
scale = count.max()/weib(x, 1., 5.).max()
plt.plot(x, weib(x, 1., 5.)*scale)
plt.show()

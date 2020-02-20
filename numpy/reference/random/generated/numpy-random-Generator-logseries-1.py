# Draw samples from the distribution:

a = .6
s = np.random.default_rng().logseries(a, 10000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s)

# #   plot against distribution

def logseries(k, p):
    return -p**k/(k*np.log(1-p))
plt.plot(bins, logseries(bins, a) * count.max()/
         logseries(bins, a).max(), 'r')
plt.show()

# Draw samples from the distribution:

loc, scale = 10, 1
s = np.random.logistic(loc, scale, 10000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, bins=50)

# #   plot against distribution

def logist(x, loc, scale):
    return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
lgst_val = logist(bins, loc, scale)
plt.plot(bins, lgst_val * count.max() / lgst_val.max())
plt.show()

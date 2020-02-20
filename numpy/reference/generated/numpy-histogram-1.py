np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
# (array([0, 2, 1]), array([0, 1, 2, 3]))
np.histogram(np.arange(4), bins=np.arange(5), density=True)
# (array([0.25, 0.25, 0.25, 0.25]), array([0, 1, 2, 3, 4]))
np.histogram([[1, 2, 1], [1, 0, 1]], bins=[0,1,2,3])
# (array([1, 4, 1]), array([0, 1, 2, 3]))

a = np.arange(5)
hist, bin_edges = np.histogram(a, density=True)
hist
# array([0.5, 0. , 0.5, 0. , 0. , 0.5, 0. , 0.5, 0. , 0.5])
hist.sum()
# 2.4999999999999996
np.sum(hist * np.diff(bin_edges))
# 1.0

# .. versionadded:: 1.11.0

# Automated Bin Selection Methods example, using 2 peak random data
# with 2000 points:

import matplotlib.pyplot as plt
rng = np.random.RandomState(10)  # deterministic random data
a = np.hstack((rng.normal(size=1000),
               rng.normal(loc=5, scale=2, size=1000)))
_ = plt.hist(a, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
# Text(0.5, 1.0, "Histogram with 'auto' bins")
plt.show()

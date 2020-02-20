np.random.random_integers(5)
# 4 # random
type(np.random.random_integers(5))
# <class 'numpy.int64'>
np.random.random_integers(5, size=(3,2))
# array([[5, 4], # random
# [3, 3],
# [4, 5]])

# Choose five random numbers from the set of five evenly-spaced
# numbers between 0 and 2.5, inclusive (*i.e.*, from the set
# :math:`{0, 5/8, 10/8, 15/8, 20/8}`):

2.5 * (np.random.random_integers(5, size=(5,)) - 1) / 4.
# array([ 0.625,  1.25 ,  0.625,  0.625,  2.5  ]) # random

# Roll two six sided dice 1000 times and sum the results:

d1 = np.random.random_integers(1, 6, 1000)
d2 = np.random.random_integers(1, 6, 1000)
dsums = d1 + d2

# Display results as a histogram:

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(dsums, 11, density=True)
plt.show()

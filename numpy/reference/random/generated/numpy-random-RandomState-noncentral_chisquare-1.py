# Draw values from the distribution and plot the histogram

import matplotlib.pyplot as plt
values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
                  bins=200, density=True)
plt.show()

# Draw values from a noncentral chisquare with very small noncentrality,
# and compare to a chisquare.

plt.figure()
values = plt.hist(np.random.noncentral_chisquare(3, .0000001, 100000),
                  bins=np.arange(0., 25, .1), density=True)
values2 = plt.hist(np.random.chisquare(3, 100000),
                   bins=np.arange(0., 25, .1), density=True)
plt.plot(values[1][0:-1], values[0]-values2[0], 'ob')
plt.show()

# Demonstrate how large values of non-centrality lead to a more symmetric
# distribution.

plt.figure()
values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
                  bins=200, density=True)
plt.show()

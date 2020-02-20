# Draw values from the distribution and plot the histogram:

import matplotlib.pyplot as plt
h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
             density=True)
plt.show()

# Draw samples from the distribution:

import numpy as np
s = np.random.poisson(5, 10000)

# Display histogram of the sample:

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 14, density=True)
plt.show()

# Draw each 100 values for lambda 100 and 500:

s = np.random.poisson(lam=(100., 500.), size=(100, 2))

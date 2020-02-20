# Draw samples and plot the distribution:

import matplotlib.pyplot as plt
s = np.random.standard_cauchy(1000000)
s = s[(s>-25) & (s<25)]  # truncate distribution so it plots well
plt.hist(s, bins=100)
plt.show()

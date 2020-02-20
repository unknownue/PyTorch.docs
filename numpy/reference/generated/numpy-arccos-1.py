# We expect the arccos of 1 to be 0, and of -1 to be pi:

np.arccos([1, -1])
# array([ 0.        ,  3.14159265])

# Plot arccos:

import matplotlib.pyplot as plt
x = np.linspace(-1, 1, num=100)
plt.plot(x, np.arccos(x))
plt.axis('tight')
plt.show()

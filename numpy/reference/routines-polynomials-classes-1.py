import matplotlib.pyplot as plt
from numpy.polynomial import Chebyshev as T
x = np.linspace(-1, 1, 100)
for i in range(6): ax = plt.plot(x, T.basis(i)(x), lw=2, label="$T_%d$"%i)
# ...
plt.legend(loc="upper left")
# <matplotlib.legend.Legend object at 0x3b3ee10>
plt.show()

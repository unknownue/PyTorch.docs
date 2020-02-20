np.cosh(0)
# 1.0

# The hyperbolic cosine describes the shape of a hanging cable:

import matplotlib.pyplot as plt
x = np.linspace(-4, 4, 1000)
plt.plot(x, np.cosh(x))
plt.show()

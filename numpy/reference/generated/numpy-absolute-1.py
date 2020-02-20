x = np.array([-1.2, 1.2])
np.absolute(x)
# array([ 1.2,  1.2])
np.absolute(1.2 + 1j)
# 1.5620499351813308

# Plot the function over ``[-10, 10]``:

import matplotlib.pyplot as plt

x = np.linspace(start=-10, stop=10, num=101)
plt.plot(x, np.absolute(x))
plt.show()

# Plot the function over the complex plane:

xx = x + 1j * x[:, np.newaxis]
plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
plt.show()

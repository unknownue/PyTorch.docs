# Plot the magnitude and phase of ``exp(x)`` in the complex plane:

import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
xx = x + 1j * x[:, np.newaxis] # a + ib over complex plane
out = np.exp(xx)

plt.subplot(121)
plt.imshow(np.abs(out),
           extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='gray')
plt.title('Magnitude of exp(x)')

plt.subplot(122)
plt.imshow(np.angle(out),
           extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='hsv')
plt.title('Phase (angle) of exp(x)')
plt.show()

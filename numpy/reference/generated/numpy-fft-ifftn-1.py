a = np.eye(4)
np.fft.ifftn(np.fft.fftn(a, axes=(0,)), axes=(1,))
# array([[1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j], # may vary
# [0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j],
# [0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
# [0.+0.j,  0.+0.j,  0.+0.j,  1.+0.j]])

# Create and plot an image with band-limited frequency content:

import matplotlib.pyplot as plt
n = np.zeros((200,200), dtype=complex)
n[60:80, 20:40] = np.exp(1j*np.random.uniform(0, 2*np.pi, (20, 20)))
im = np.fft.ifftn(n).real
plt.imshow(im)
# <matplotlib.image.AxesImage object at 0x...>
plt.show()

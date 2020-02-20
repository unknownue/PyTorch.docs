np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))
# array([-2.33486982e-16+1.14423775e-17j,  8.00000000e+00-1.25557246e-15j,
# 2.33486982e-16+2.33486982e-16j,  0.00000000e+00+1.22464680e-16j,
# -1.14423775e-17+2.33486982e-16j,  0.00000000e+00+5.20784380e-16j,
# 1.14423775e-17+1.14423775e-17j,  0.00000000e+00+1.22464680e-16j])

# In this example, real input has an FFT which is Hermitian, i.e., symmetric
# in the real part and anti-symmetric in the imaginary part, as described in
# the `numpy.fft` documentation:

import matplotlib.pyplot as plt
t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)
# [<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
plt.show()

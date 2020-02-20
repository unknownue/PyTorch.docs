np.hamming(12)
# array([ 0.08      ,  0.15302337,  0.34890909,  0.60546483,  0.84123594, # may vary
# 0.98136677,  0.98136677,  0.84123594,  0.60546483,  0.34890909,
# 0.15302337,  0.08      ])

# Plot the window and the frequency response:

import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
window = np.hamming(51)
plt.plot(window)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Hamming window")
# Text(0.5, 1.0, 'Hamming window')
plt.ylabel("Amplitude")
# Text(0, 0.5, 'Amplitude')
plt.xlabel("Sample")
# Text(0.5, 0, 'Sample')
plt.show()

plt.figure()
# <Figure size 640x480 with 0 Axes>
A = fft(window, 2048) / 25.5
mag = np.abs(fftshift(A))
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(mag)
response = np.clip(response, -100, 100)
plt.plot(freq, response)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Frequency response of Hamming window")
# Text(0.5, 1.0, 'Frequency response of Hamming window')
plt.ylabel("Magnitude [dB]")
# Text(0, 0.5, 'Magnitude [dB]')
plt.xlabel("Normalized frequency [cycles per sample]")
# Text(0.5, 0, 'Normalized frequency [cycles per sample]')
plt.axis('tight')
# ...
plt.show()

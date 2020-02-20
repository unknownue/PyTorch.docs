np.hanning(12)
# array([0.        , 0.07937323, 0.29229249, 0.57115742, 0.82743037,
# 0.97974649, 0.97974649, 0.82743037, 0.57115742, 0.29229249,
# 0.07937323, 0.        ])

# Plot the window and its frequency response:

import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
window = np.hanning(51)
plt.plot(window)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Hann window")
# Text(0.5, 1.0, 'Hann window')
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
with np.errstate(divide='ignore', invalid='ignore'):
    response = 20 * np.log10(mag)
# ...
response = np.clip(response, -100, 100)
plt.plot(freq, response)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Frequency response of the Hann window")
# Text(0.5, 1.0, 'Frequency response of the Hann window')
plt.ylabel("Magnitude [dB]")
# Text(0, 0.5, 'Magnitude [dB]')
plt.xlabel("Normalized frequency [cycles per sample]")
# Text(0.5, 0, 'Normalized frequency [cycles per sample]')
plt.axis('tight')
# ...
plt.show()

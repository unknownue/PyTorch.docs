import matplotlib.pyplot as plt
np.bartlett(12)
# array([ 0.        ,  0.18181818,  0.36363636,  0.54545455,  0.72727273, # may vary
# 0.90909091,  0.90909091,  0.72727273,  0.54545455,  0.36363636,
# 0.18181818,  0.        ])

# Plot the window and its frequency response (requires SciPy and matplotlib):

from numpy.fft import fft, fftshift
window = np.bartlett(51)
plt.plot(window)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Bartlett window")
# Text(0.5, 1.0, 'Bartlett window')
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
plt.title("Frequency response of Bartlett window")
# Text(0.5, 1.0, 'Frequency response of Bartlett window')
plt.ylabel("Magnitude [dB]")
# Text(0, 0.5, 'Magnitude [dB]')
plt.xlabel("Normalized frequency [cycles per sample]")
# Text(0.5, 0, 'Normalized frequency [cycles per sample]')
_ = plt.axis('tight')
plt.show()

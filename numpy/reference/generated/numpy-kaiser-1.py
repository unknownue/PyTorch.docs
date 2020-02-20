import matplotlib.pyplot as plt
np.kaiser(12, 14)
# array([7.72686684e-06, 3.46009194e-03, 4.65200189e-02, # may vary
# 2.29737120e-01, 5.99885316e-01, 9.45674898e-01,
# 9.45674898e-01, 5.99885316e-01, 2.29737120e-01,
# 4.65200189e-02, 3.46009194e-03, 7.72686684e-06])

# Plot the window and the frequency response:

from numpy.fft import fft, fftshift
window = np.kaiser(51, 14)
plt.plot(window)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Kaiser window")
# Text(0.5, 1.0, 'Kaiser window')
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
plt.title("Frequency response of Kaiser window")
# Text(0.5, 1.0, 'Frequency response of Kaiser window')
plt.ylabel("Magnitude [dB]")
# Text(0, 0.5, 'Magnitude [dB]')
plt.xlabel("Normalized frequency [cycles per sample]")
# Text(0.5, 0, 'Normalized frequency [cycles per sample]')
plt.axis('tight')
# (-0.5, 0.5, -100.0, ...) # may vary
plt.show()

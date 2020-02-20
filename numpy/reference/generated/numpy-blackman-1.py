import matplotlib.pyplot as plt
np.blackman(12)
# array([-1.38777878e-17,   3.26064346e-02,   1.59903635e-01, # may vary
# 4.14397981e-01,   7.36045180e-01,   9.67046769e-01,
# 9.67046769e-01,   7.36045180e-01,   4.14397981e-01,
# 1.59903635e-01,   3.26064346e-02,  -1.38777878e-17])

# Plot the window and the frequency response:

from numpy.fft import fft, fftshift
window = np.blackman(51)
plt.plot(window)
# [<matplotlib.lines.Line2D object at 0x...>]
plt.title("Blackman window")
# Text(0.5, 1.0, 'Blackman window')
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
plt.title("Frequency response of Blackman window")
# Text(0.5, 1.0, 'Frequency response of Blackman window')
plt.ylabel("Magnitude [dB]")
# Text(0, 0.5, 'Magnitude [dB]')
plt.xlabel("Normalized frequency [cycles per sample]")
# Text(0.5, 0, 'Normalized frequency [cycles per sample]')
_ = plt.axis('tight')
plt.show()

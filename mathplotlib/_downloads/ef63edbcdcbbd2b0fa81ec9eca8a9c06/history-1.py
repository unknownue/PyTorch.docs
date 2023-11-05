from matplotlib import cbook, pyplot as plt, style
import numpy as np

style.use("classic")

datafile = cbook.get_sample_data('membrane.dat', asfileobj=False)

# convert data to mV
x = 1000 * 0.1 * np.fromstring(open(datafile, 'rb').read(), np.float32)
# 0.0005 is the sample interval
t = 0.0005 * np.arange(len(x))
plt.figure(1, figsize=(7, 1), dpi=100)
ax = plt.subplot(111, facecolor='y')
plt.plot(t, x)
plt.text(0.5, 0.5, 'matplotlib', color='r',
         fontsize=40, fontname=['Courier', 'DejaVu Sans Mono'],
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax.transAxes,
         )
plt.axis([1, 1.72, -60, 10])
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
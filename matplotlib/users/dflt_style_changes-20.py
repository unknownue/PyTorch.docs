import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.15, wspace=0.3, left=0.09, right=0.95)

x = np.linspace(2000, 2008, 9)
y = np.random.randn(9) + 50000

with plt.rc_context(rc={'axes.formatter.offset_threshold' : 2}):
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(x, y)
    ax1.set_title('classic')

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, y)
ax2.set_title('v2.0')
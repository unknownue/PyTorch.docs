import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy

data = np.zeros(1000)
data[0] = 1

fig = plt.figure(figsize=(6, 3))

def demo(fig, rc, title, j):
    with mpl.rc_context(rc=rc):
        ax = fig.add_subplot(1, 2, j)
        ax.plot(data)
        ax.set_title(title)

demo(fig, {'axes.autolimit_mode': 'round_numbers',
           'axes.xmargin': 0,
           'axes.ymargin': 0}, 'classic', 1)
demo(fig, {}, 'v2.0', 2)
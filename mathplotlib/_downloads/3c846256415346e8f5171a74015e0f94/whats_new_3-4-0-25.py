fig, ax = plt.subplots(2, 1, figsize=(5, 1))
fig.subplots_adjust(left=0.2, right=0.8)

from matplotlib.widgets import Slider, RangeSlider
Slider(ax[0], 'Slider', 0, 1)
RangeSlider(ax[1], 'RangeSlider', 0, 1)
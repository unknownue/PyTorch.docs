from matplotlib import pyplot as plt
from matplotlib.widgets import TextBox

fig = plt.figure(figsize=(4, 3))
for i, alignment in enumerate(['left', 'center', 'right']):
        box_input = fig.add_axes([0.1, 0.7 - i*0.3, 0.8, 0.2])
        text_box = TextBox(ax=box_input, initial=f'{alignment} alignment',
                           label='', textalignment=alignment)
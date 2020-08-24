from __future__ import unicode_literals

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
tick_labels = ['😃', '😎', '😴', '😲', '😻']
bar_labels = ['א', 'α', '☣', '⌬', 'ℝ']
y = [1, 4, 9, 16, 25]
x = range(5)
ax.bar(x, y, tick_label=tick_labels, align='center')
ax.xaxis.set_tick_params(labelsize=20)
for _x, _y, t in zip(x, y, bar_labels):
    ax.annotate(t, (_x, _y), fontsize=20, ha='center',
                xytext=(0, -2), textcoords='offset pixels',
                bbox={'facecolor': 'w'})

ax.set_title('Диаграмма со смайликами')
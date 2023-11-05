import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(layout='constrained')
date_first = np.datetime64('2020-01-01', 'D')
date_last = np.datetime64('2020-01-11', 'D')

arr = [[i+j for i in range(10)] for j in range(10)]

ax.imshow(arr, origin='lower', extent=[0, 10, date_first, date_last])

plt.show()
import numpy
import matplotlib.pyplot as plt

np.random.seed(19680801)
n= 300
x = np.random.standard_normal(n)
y = np.random.standard_normal(n)

fig, ax = plt.subplots(figsize=(4, 4))
h = ax.hexbin(x, y, gridsize=(5, 3))
hx, hy = h.get_offsets().T
ax.plot(hx[24::3], hy[24::3], 'ro-')
ax.plot(hx[-3:], hy[-3:], 'ro-')
ax.set_title('gridsize=(5, 3)')
ax.axis('off')
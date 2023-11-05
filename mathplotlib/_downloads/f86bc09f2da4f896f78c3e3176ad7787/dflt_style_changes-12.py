import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'

fig, ax = plt.subplots(tight_layout=True, figsize=(3, 3))

ax.plot(range(15), label=r'int: $15 \int_0^\infty dx$')
ax.legend()
ax.set_title('classic')
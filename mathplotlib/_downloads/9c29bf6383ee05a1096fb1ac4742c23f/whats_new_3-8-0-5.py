import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

rectangle = Rectangle((.2, .2), .6, .6,
                      facecolor=('blue', 0.2),
                      edgecolor=('green', 0.5))
ax.add_patch(rectangle)
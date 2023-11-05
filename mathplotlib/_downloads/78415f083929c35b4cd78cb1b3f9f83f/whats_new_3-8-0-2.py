import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.ecdf(np.random.randn(100))
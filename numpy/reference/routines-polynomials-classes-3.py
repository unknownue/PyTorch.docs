import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Chebyshev as T
np.random.seed(11)
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x) + np.random.normal(scale=.1, size=x.shape)
p = T.fit(x, y, 5)
plt.plot(x, y, 'o')
# [<matplotlib.lines.Line2D object at 0x2136c10>]
xx, yy = p.linspace()
plt.plot(xx, yy, lw=2)
# [<matplotlib.lines.Line2D object at 0x1cf2890>]
p.domain
# array([ 0.        ,  6.28318531])
p.window
# array([-1.,  1.])
plt.show()

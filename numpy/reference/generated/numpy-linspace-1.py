np.linspace(2.0, 3.0, num=5)
# array([2.  , 2.25, 2.5 , 2.75, 3.  ])
np.linspace(2.0, 3.0, num=5, endpoint=False)
# array([2. ,  2.2,  2.4,  2.6,  2.8])
np.linspace(2.0, 3.0, num=5, retstep=True)
# (array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)

# Graphical illustration:

import matplotlib.pyplot as plt
N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
plt.plot(x1, y, 'o')
# [<matplotlib.lines.Line2D object at 0x...>]
plt.plot(x2, y + 0.5, 'o')
# [<matplotlib.lines.Line2D object at 0x...>]
plt.ylim([-0.5, 1])
# (-0.5, 1)
plt.show()

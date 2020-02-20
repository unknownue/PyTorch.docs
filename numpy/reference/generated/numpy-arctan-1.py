# We expect the arctan of 0 to be 0, and of 1 to be pi/4:

np.arctan([0, 1])
# array([ 0.        ,  0.78539816])

np.pi/4
# 0.78539816339744828

# Plot arctan:

import matplotlib.pyplot as plt
x = np.linspace(-10, 10)
plt.plot(x, np.arctan(x))
plt.axis('tight')
plt.show()

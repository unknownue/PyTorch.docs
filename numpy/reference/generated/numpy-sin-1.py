# Print sine of one angle:

np.sin(np.pi/2.)
# 1.0

# Print sines of an array of angles given in degrees:

np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180. )
# array([ 0.        ,  0.5       ,  0.70710678,  0.8660254 ,  1.        ])

# Plot the sine function:

import matplotlib.pylab as plt
x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = y = np.linspace(0., 2*np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X) * np.sin(0.5*Y)

clevs = [-.75, -.5, -.25, 0., .25, .5, .75]
cmap = plt.cm.get_cmap(name='jet', lut=8)

ax1 = plt.subplot(211)
cs1 = plt.contourf(x, y, Z, clevs, cmap=cmap, extend='both')
cb1 = plt.colorbar(orientation='horizontal', extendfrac=None)
cb1.set_label('Default length colorbar extensions')

ax2 = plt.subplot(212)
cs2 = plt.contourf(x, y, Z, clevs, cmap=cmap, extend='both')
cb2 = plt.colorbar(orientation='horizontal', extendfrac='auto')
cb2.set_label('Custom length colorbar extensions')

plt.show()
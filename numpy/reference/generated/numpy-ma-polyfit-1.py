import warnings
x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit(x, y, 3)
z
# array([ 0.08703704, -0.81349206,  1.69312169, -0.03968254]) # may vary

# It is convenient to use `poly1d` objects for dealing with polynomials:

p = np.poly1d(z)
p(0.5)
# 0.6143849206349179 # may vary
p(3.5)
# -0.34732142857143039 # may vary
p(10)
# 22.579365079365115 # may vary

# High-order polynomials may oscillate wildly:

with warnings.catch_warnings():
    warnings.simplefilter('ignore', np.RankWarning)
    p30 = np.poly1d(np.polyfit(x, y, 30))
# ...
p30(4)
# -0.80000000000000204 # may vary
p30(5)
# -0.99999999999999445 # may vary
p30(4.5)
# -0.10547061179440398 # may vary

# Illustration:

import matplotlib.pyplot as plt
xp = np.linspace(-2, 6, 100)
_ = plt.plot(x, y, '.', xp, p(xp), '-', xp, p30(xp), '--')
plt.ylim(-2,2)
# (-2, 2)
plt.show()

# Taking an example cited in Wikipedia, this distribution can be used if
# one wanted to cut strings (each of initial length 1.0) into K pieces
# with different lengths, where each piece had, on average, a designated
# average length, but allowing some variation in the relative sizes of
# the pieces.

s = np.random.default_rng().dirichlet((10, 5, 3), 20).transpose()

import matplotlib.pyplot as plt
plt.barh(range(20), s[0])
plt.barh(range(20), s[1], left=s[0], color='g')
plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
plt.title("Lengths of Strings")

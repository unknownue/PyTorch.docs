# In a study, testing for a specific alternative to the null hypothesis
# requires use of the Noncentral F distribution. We need to calculate the
# area in the tail of the distribution that exceeds the value of the F
# distribution for the null hypothesis.  We'll plot the two probability
# distributions for comparison.

rng = np.random.default_rng()
dfnum = 3 # between group deg of freedom
dfden = 20 # within groups degrees of freedom
nonc = 3.0
nc_vals = rng.noncentral_f(dfnum, dfden, nonc, 1000000)
NF = np.histogram(nc_vals, bins=50, density=True)
c_vals = rng.f(dfnum, dfden, 1000000)
F = np.histogram(c_vals, bins=50, density=True)
import matplotlib.pyplot as plt
plt.plot(F[1][1:], F[0])
plt.plot(NF[1][1:], NF[0])
plt.show()

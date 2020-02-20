# From Dalgaard page 83 [R89f5270d198b-1]_, suppose the daily energy intake for 11
# women in kilojoules (kJ) is:

intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \
                   7515, 8230, 8770])

# Does their energy intake deviate systematically from the recommended
# value of 7725 kJ?

# We have 10 degrees of freedom, so is the sample mean within 95% of the
# recommended value?

s = np.random.standard_t(10, size=100000)
np.mean(intake)
# 6753.636363636364
intake.std(ddof=1)
# 1142.1232221373727

# Calculate the t statistic, setting the ddof parameter to the unbiased
# value so the divisor in the standard deviation will be degrees of
# freedom, N-1.

t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))
import matplotlib.pyplot as plt
h = plt.hist(s, bins=100, density=True)

# For a one-sided t-test, how far out in the distribution does the t
# statistic appear?

np.sum(s<t) / float(len(s))
# 0.0090699999999999999  #random

# So the p-value is about 0.009, which says the null hypothesis has a
# probability of about 99% of being true.

import numpy as np
import matplotlib.pyplot as plt

data = np.random.lognormal(size=(37, 4))
fig, (old, new) = plt.subplots(ncols=2, sharey=True)
with plt.style.context('default'):
    new.boxplot(data, labels=['A', 'B', 'C', 'D'])
    new.set_title('v2.0')

with plt.style.context('classic'):
    old.boxplot(data, labels=['A', 'B', 'C', 'D'])
    old.set_title('classic')

new.set_yscale('log')
old.set_yscale('log')
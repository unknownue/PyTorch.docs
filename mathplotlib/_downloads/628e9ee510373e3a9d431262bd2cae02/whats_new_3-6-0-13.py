plt.figure()
plt.plot([1, 2, 3, 3.5], [2, 1, 0, -0.5])
plt.xticks([1, 2, 3], ["One", "Zwei", "Trois"])
plt.xticks([np.sqrt(2), 2.5, np.pi],
           [r"$\sqrt{2}$", r"$\frac{5}{2}$", r"$\pi$"], minor=True)
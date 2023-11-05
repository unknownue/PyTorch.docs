arr = np.arange(12).reshape((3, 4))

fig, ax = plt.subplots()
pc = ax.pcolor(arr)

# Mask one element and show that the hatch is also not drawn
# over that region
pc.set_array(np.ma.masked_equal(arr, 5))
pc.set_hatch('//')

plt.show()
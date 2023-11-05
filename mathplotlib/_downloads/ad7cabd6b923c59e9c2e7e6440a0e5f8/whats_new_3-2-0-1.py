import matplotlib.pyplot as plt

# Use old kerning values:
plt.rcParams['text.kerning_factor'] = 6
fig, ax = plt.subplots()
ax.text(0.0, 0.05, 'BRAVO\nAWKWARD\nVAT\nW.Test', fontsize=56)
ax.set_title('Before (text.kerning_factor = 6)')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(5, 5))
t = ax.text(0.5, 0.5, "elliptical box",
        ha="center", size=15,
        bbox=dict(boxstyle="ellipse,pad=0.3"))
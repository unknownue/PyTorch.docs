import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(4, 2), facecolor='lightskyblue')
ax.set_position([0.1, 0.2, 0.8, 0.7])
ax.set_aspect(1)
bb = ax.get_tightbbox()
bb = bb.padded(10)
bb = bb.transformed(fig.dpi_scale_trans.inverted())
fancy = FancyBboxPatch(bb.p0, bb.width, bb.height, fc='none',
                       ec=(0, 0.0, 0, 0.5), lw=2, linestyle='--',
                       transform=fig.dpi_scale_trans,
                       clip_on=False, boxstyle='Square, pad=0')
ax.add_patch(fancy)
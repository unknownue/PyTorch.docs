# Original (previously combined with below) rcParams:
plt.rcParams['figure.titlesize'] = 64
plt.rcParams['figure.titleweight'] = 'bold'

# New rcParams:
plt.rcParams['figure.labelsize'] = 32
plt.rcParams['figure.labelweight'] = 'bold'

fig, axs = plt.subplots(2, 2, layout='constrained')
for ax in axs.flat:
    ax.set(xlabel='xlabel', ylabel='ylabel')

fig.suptitle('suptitle')
fig.supxlabel('supxlabel')
fig.supylabel('supylabel')
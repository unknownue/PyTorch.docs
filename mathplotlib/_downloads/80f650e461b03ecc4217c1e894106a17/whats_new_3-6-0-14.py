fig, axs = plt.subplots(3, 1)
for i, alignment in enumerate(['left', 'center', 'right']):
    axs[i].plot(range(10), label='test')
    axs[i].legend(title=f'{alignment=}', alignment=alignment)
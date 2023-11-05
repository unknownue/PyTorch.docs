import matplotlib.pyplot as plt
with plt.rc_context({'axes3d.xaxis.panecolor': (0.9, 0.0, 0.0, 0.5),
                     'axes3d.yaxis.panecolor': (0.7, 0.0, 0.0, 0.5),
                     'axes3d.zaxis.panecolor': (0.8, 0.0, 0.0, 0.5)}):
    fig = plt.figure()
    fig.add_subplot(projection='3d')
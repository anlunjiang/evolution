import matplotlib.pyplot as plt
import matplotlib.animation as animation
from nptyping import Array

from world_jobs import update_world


def animate(grid: Array, update_interval: int):

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    a = animation.FuncAnimation(fig, update_world, fargs=(img, grid),
                                interval=update_interval,
                                blit=True)

    plt.show()

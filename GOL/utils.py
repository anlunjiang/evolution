import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from nptyping import Array
from typing import Tuple


def init_world(n: int, clean: bool) -> Array:

    if clean:
        grid = np.zeros(n * n).reshape(n, n)
        grid = setup_init(grid, 1, 1)
        return grid

    grid = np.random.choice([0, 255], n * n, p=[0.9, 0.1]).reshape(n, n)
    grid = setup_init(grid, 1, 1)
    return grid


def setup_init(grid: Array, x: int, y: int) -> Array:
    start = np.array([
        [0,   0,   255],
        [255, 0,   255],
        [0,   255, 255],
    ])
    grid[x:x+3, y:y+3] = start
    return grid


def update_world(frame: int, img: Array, grid: Array) -> Tuple:

    # Ensure that the matrix world is square
    assert grid.shape[0] == grid.shape[1]
    n = grid.shape[0]
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    new = grid.copy()
    # Copy grid since iterating will affect the result of the next step
    nbr_cnt = convolve(grid, kernel, mode='constant') / 255

    for i in range(n):
        for j in range(n):

            if grid[i, j] == 255:
                if (nbr_cnt[i, j] < 2) or (nbr_cnt[i, j] > 3):
                    new[i, j] = 0

            if nbr_cnt[i, j] == 3:
                new[i, j] = 255

    img.set_data(new)
    grid[:] = new[:]
    return img,


def animate(grid: Array, update_interval: int):

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    a = animation.FuncAnimation(fig, update_world, fargs=(img, grid),
                                interval=update_interval,
                                blit=True)

    plt.show()

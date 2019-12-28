import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def init_world(n):
    grid = np.zeros(n * n).reshape(n, n)
    grid = setup_init(grid, 20, 20)
    return grid


def setup_init(grid, x, y):
    start = np.array([
        [0,   0,   255],
        [255, 0,   255],
        [0,   255, 255],
    ])
    grid[x:x+3, y:y+3] = start
    return grid


def update(frame, img, grid):
    print('updating')
    # Ensure that the matrix world is square
    assert grid.shape[0] == grid.shape[1]
    n = grid.shape[0]
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    new = grid.copy()
    nbr_cnt = convolve(grid, kernel, mode='constant') / 255

    for i in range(n):
        for j in range(n):

            if grid[i, j] == 255:
                if (nbr_cnt[i, j] < 2) or (nbr_cnt[i, j] > 3):
                    new[i, j] = 0

            if nbr_cnt[i, j] > 3:
                new[i, j] = 255

    img.set_data(new)
    grid[:] = new[:]
    return img


def animate(grid, update_interval):

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    animation.FuncAnimation(fig, update, fargs=(img, grid),
                            interval=update_interval)
    plt.show()






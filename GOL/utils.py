import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.ndimage import convolve

on = 255
off = 0

n = 100


def init_world(n):
    grid = np.zeros(n * n).reshape(n, n)
    grid = setup_init(grid, 1, 1)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    plt.show()
    return grid


def setup_init(grid, x ,y):
    kernel = np.array([
        [0,   0,   255],
        [255, 0,   255],
        [0,   255, 255],
    ])
    grid[x:x+3, y:y+3] = kernel
    return grid


def update_world(grid):

    assert grid.shape[0] == grid.shape[1]
    # Ensure that the matrix world is square
    for row in range(n):
        for col in range(n):
            sum_of_neighbours =



    return

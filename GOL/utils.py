import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


on = 255
off = 0

n = 100


def init_world(n):
    grid = np.zeros(n * n).reshape(n, n)
    grid = setup_init(grid, 1, 1)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    print(grid)
    plt.show()


def setup_init(grid, x ,y):
    start_condition = np.array([
        [0,   0,   255],
        [255, 0,   255],
        [0,   255, 255],
    ])
    grid[x:x+3, y:y+3] = start_condition
    return grid


def cycle():

    return

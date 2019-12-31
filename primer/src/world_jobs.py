import random
import matplotlib.pyplot as plt
from constants import *


class create_blob(object):

    spawn_count = 0

    def __init__(self, nm):
        self.id = nm
        create_blob.spawn_count += 1

    def death(self):
        create_blob.spawn_count -= 1

blob_list = []
spawncount_list = []
xdata = []

def update_world(frame, plot, birth_chance, death_chance, replicate_chance):

    spawncount_list.append(calculate(frame, birth_chance, death_chance, replicate_chance))

    xdata.append(frame)
    ydata = spawncount_list
    avg = sum(spawncount_list) / len(spawncount_list)
    plot.clear()
    plot.plot(xdata, ydata)

    plt.xlabel('Iteration')
    plt.ylabel('Number')
    plt.title('Animation of Simulation')
    plt.xlim((0, iterations))

    return plot,

def calculate(frame, birth_chance, death_chance, replicate_chance):

    if random.random() <= birth_chance:
        blob = create_blob(frame)
        blob_list.append(blob)

    for j in blob_list:
        if random.random() <= replicate_chance:
            blob = create_blob(len(blob_list) + 1)
            blob_list.append(blob)
        if random.random() <= death_chance:
            j.death()
            blob_list.remove(j)
    return create_blob.spawn_count





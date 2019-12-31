import matplotlib.pyplot as plt
import matplotlib.animation as animation

from world_jobs import update_world


def animate(update_interval: int,
            birth_chance,
            death_chance,
            replicate_chance,
            iterations):

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    a = animation.FuncAnimation(fig, update_world,
                                fargs=(ax1, birth_chance, death_chance, replicate_chance),
                                interval=update_interval,
                                frames=iterations,
                                blit=False,
                                repeat=False)

    print(f'Birth chance: {birth_chance}')
    print(f'Replication chance: {replicate_chance}')
    print(f'Death chance: {death_chance}')
    #print(f'Average number of blobs: {avg}')
    plt.show()

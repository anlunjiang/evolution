import argparse

from utils import init_world, animate


def main():

    update_interval = 50

    args = parser_args_run()

    grid = init_world(int(args.grid_size))

    animate(grid, int(args.interval))

    return



def parser_args_run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--grid-size',
                        help='grid size of the world to be initiated',
                        default=50
                        )
    parser.add_argument('--interval',
                        help='interval in ms between frames',
                        default=100
                        )
    return parser.parse_args()


if __name__ == '__main__':
    main()

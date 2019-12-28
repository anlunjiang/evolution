import argparse

from utils import init_world, animate


def main():

    args = parser_args_run()

    grid = init_world(int(args.grid_size), args.clean)

    animate(grid, int(args.interval))

def parser_args_run():

    parser = argparse.ArgumentParser()
    parser.add_argument('--grid-size',
                        help='grid size of the world to be initiated',
                        default=100
                        )
    parser.add_argument('--interval',
                        help='interval in ms between frames',
                        default=30
                        )
    parser.add_argument('--clean',
                        help='specify to have a clean world with only specified object',
                        action='store_true'
                        )
    return parser.parse_args()


if __name__ == '__main__':
    main()

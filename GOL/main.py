import argparse

from utils import init_world, update_world


def main():
    args = parser_args_run()

    init_world(int(args.grid_size))

    return



def parser_args_run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--grid-size',
                        help='grid size of the world to be initiated',
                        default=100
                        )
    return parser.parse_args()


if __name__ == '__main__':
    main()

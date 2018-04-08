import logging
from .akttym import akttym


def main():
    akttym()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

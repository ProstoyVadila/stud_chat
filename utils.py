import logging
import sys


def get_logger():
    date_format = '%d-%b-%y %H:%M:%S'
    format = '%(asctime)s - | %(levelname)s | - %(message)s'
    level = logging.INFO
    if '-d' in sys.argv[1:]:
        level = logging.DEBUG

    logging.basicConfig(format=format, datefmt=date_format, level=level)


class InitAppException(Exception):
    pass

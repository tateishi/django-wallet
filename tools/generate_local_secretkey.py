#! /usr/bin/env python

import sys
from django.core.management.utils import get_random_secret_key


def main(out=sys.stdout):
    secret_key = get_random_secret_key()
    print(f'SECRET_KEY = \'{secret_key}\'', file=out)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], mode='w') as out:
            main(out)
    else:
        main()

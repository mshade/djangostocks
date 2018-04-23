#!/usr/bin/env python3

from os.path import isfile
from django.core.management import utils

# Bail if .env exists already
if isfile('.env'):
    print('.env file already present; exiting.')
    exit(0)


try:
    new_secret = utils.get_random_secret_key()
    with open('example.env','rt') as env_in:
        with open('.env', 'wt') as env_out:
            for line in env_in:
                env_out.write(line.replace('replaceme', new_secret))
    print('.env written.')
except OSError as err:
    print('OS Error: {}'.format(err))
except:
    print('Unexpected error.')

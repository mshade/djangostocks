#!/usr/bin/env python3

from django.core.management import utils

new_secret = utils.get_random_secret_key()

try:
    with open('example.env','rt') as env_in:
        with open('.env', 'wt') as env_out:
            for line in env_in:
                env_out.write(line.replace('replaceme', new_secret))
    print('.env written.')
except OSError as err:
    print('OS Error: {}'.format(err))
except:
    print('Unexpected error.')

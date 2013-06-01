# -*- coding: utf-8 -*-
'''Entrypoint module, in case you use `python -m userifc_py.demo`.'''

import sys

from userifc_py.demo import cli

if '__main__' == __name__:
    cli.main(sys.argv[1:])

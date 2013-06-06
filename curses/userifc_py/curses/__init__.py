# -*- coding: utf-8 -*-
'''Curses sub-package for Python User interface examples project.'''
from __future__ import (absolute_import, unicode_literals)

import os, sys, logging, json

# add {wheel,egg,jar}/site-packages to sys.path
if __package__ in ['', None]:
    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    sys.path.extend([os.path.join(path, 'site-packages')])

#from future.builtins import map, str

from intro_py import util


_rsrc_path = os.environ.get('RSRC_PATH')
_json_str = util.read_resource('pkginfo.json', pkg_or_mod=__name__, rsrc_path=_rsrc_path)
pkginfo = json.loads(_json_str) if _json_str is not None else {}

__version__ = pkginfo['version']    # __version__ = 'X.Y.Z'
__date__ = '2013-06-06'
__author__ = '{0} <{1}>'.format(pkginfo['author'], pkginfo['author_email'])
__credits__ = '; '.join(map(str, [pkginfo['author']]))
__license__ = pkginfo['license']
__year__ = '2013'
__copyright__ = '(c) {0}, {1}'.format(__year__, pkginfo['author'])

logging.getLogger(__name__).addHandler(logging.NullHandler())

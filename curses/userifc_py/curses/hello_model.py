# -*- coding: utf-8 -*-
'''Hello-Model module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import subject

__all__ = ['HelloModel']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloModel(subject.Subject):
  '''Description:: '''

  def __init__(self, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    super(HelloModel, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._hellopfx = util.read_resource(greetpath, pkg_or_mod=pkg_or_mod,
      rsrc_path=rsrc_path).strip('\n')

  def notifyObservers(self, arg):
    for obs in self._observers:
      obs.update('{0}{1}!'.format(self._hellopfx,
        arg if arg is not None else ''))

  
def lib_main(argv=None):
  from userifc_py.curses import hello_model, hello_view

  mod = hello_model.HelloModel('greet.txt')
  view1 = hello_view.HelloView()

  mod.attachObserver(view1)
  mod.notifyObservers('To be set -- HELP.')
  print('view1.data:', view1.data)
  return 0

if '__main__' == __name__:
  sys.exit(lib_main(sys.argv[1:]))

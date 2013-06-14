# -*- coding: utf-8 -*-
'''Hello-Model module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import subject

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')
  
from javafx.scene import Scene
from javafx.application import Application

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

class JfxApp(Application):
  def start(self, stagePrime):
    params = self.getParameters()
    param0 = params.getRaw()[0] if 0 < len(params.getRaw()) else ''
    
    from userifc_py.javafx import hello_model, hello_formview
    
    mod = hello_model.HelloModel('greet.txt')
    view1 = hello_formview.HelloView()
    
    mod.attachObserver(view1)
    mod.notifyObservers(params.getNamed()['data'])
    print('view1.data:', view1.data)
    stagePrime.setScene(Scene(view1.parent, 200, 160))
    stagePrime.show()
    
    stagePrime.close()

def lib_main(argv=None):
  data = 'To be set -- HELP.'
  
  #JfxApp.launch(JfxApp, ['--data=' + data])
  Application.launch(JfxApp, ['--data=' + data])
  
  return 0

if '__main__' == __name__:
  sys.exit(lib_main(sys.argv[1:]))

# -*- coding: utf-8 -*-
'''Swing interface builder Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')

VERSION_UIFORMSWING = os.getenv('VERSION_UIFORMSWING', '2013.04')
HERE = os.path.dirname(__file__)
#sys.path.extend([os.path.join(HERE, 'uiform_swing-{0}.jar'.format(VERSION_UIFORMSWING))])
sys.path.extend(['{0}/.m2/repository/org/sandbox/uiform_swing/{1}/uiform_swing-{1}.jar'.format(os.getenv('HOME', '.'), VERSION_UIFORMSWING)])

from org.sandbox.uiform_swing import HelloFormSwing

__all__ = ['HelloView']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(observer.Observer):
  '''Description:: '''

  def __init__(self, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.widgets, form = {}, HelloFormSwing()
    self.widgets.update({'frame1': form, 'label1': form.getjLabel1(),
			'button1': form.getjButton1(), 'textview1': form.getjTextView1(),
			'dialog1': form.getjDialog1(), 'entry1': form.getjEntry1()})

  def update(self, data):
    self._data = data
    self.widgets['textview1'].text = self.data

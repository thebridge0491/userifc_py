# -*- coding: utf-8 -*-
'''JavaFX interface builder Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')

from java.io import ByteArrayInputStream, FileInputStream
from java.net import URL

#from javafx.embed.swing import JFXPanel
#_ = JFXPanel() # ? prevent JavaFX Toolkit not initialized exception
from javafx.fxml import FXMLLoader

_uiform = 'jvm_ui/helloForm-javafx.fxml'

__all__ = ['HelloView']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(observer.Observer):
  '''Description:: '''

  def __init__(self, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''
    import io, tempfile

    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.widgets = {}
    uifile_bytes = util.read_resource(_uiform, pkg_or_mod=pkg_or_mod,
      rsrc_path=rsrc_path).encode()
    ui_tempdes, ui_temppath = tempfile.mkstemp()
    with os.fdopen(ui_tempdes, 'w') as fOut:
      fOut.write(uifile_bytes.decode('utf-8'))
      fOut.close()
    #self.parent = FXMLLoader.load(URL('file:' + ui_temppath))
    fxmlloader = FXMLLoader()
    self.parent = fxmlloader.load(FileInputStream(ui_temppath))
    #self.parent = fxmlloader.load(ByteArrayInputStream(uifile_bytes))
    self.widgets.update({'parent': self.parent.lookup('#stackpane1'),
      'pane1': self.parent.lookup('#pane1'),
      'vbox1': self.parent.lookup('#vbox1'),
      'label1': self.parent.lookup('#label1'),
      'button1': self.parent.lookup('#button1'),
      'textview1': self.parent.lookup('#textview1'),
      'dialog1': self.parent.lookup('#dialog1'),
      'entry1': self.parent.lookup('#entry1')})

  def update(self, data):
    self._data = data
    self.widgets['textview1'].text = self.data

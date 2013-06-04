# -*- coding: utf-8 -*-
'''QtQuick interface builder Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

os.environ['QT_QUICK_BACKEND'] = os.environ.get('QT_QUICK_BACKEND', 'software')

if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
  from PySide2 import QtCore, QtGui, QtWidgets, QtQml
  from PySide2.QtCore import Slot
  #from PyQt5 import sip, Qt, QtCore, QtWidgets, QtQml
  #Slot = QtCore.pyqtSlot
  #sip.setapi('QVariant', 2)
  QApplication = QtWidgets.QApplication
  _uiform = 'qt/helloForm-qt5.qml'
else:
  from PySide import QtCore, QtGui, QtQml
  from PySide.QtCore import Slot
  #from PyQt4 import Qt, QtCore, QtGui, QtDeclarative
  #Slot = QtCore.pyqtSlot
  #import sip
  #sip.setapi('QVariant', 2)
  QApplication = QtGui.QApplication
  _uiform = 'qt/helloForm-qt4.qml'

__all__ = ['HelloView', 'QtCore', 'QApplication']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(QtCore.QObject, observer.Observer):
  '''Description:: '''

  def __init__(self, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''
    import io, tempfile

    QtCore.QObject.__init__(self, None)
    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.widgets = {}
    ui_tempdes, ui_temppath = tempfile.mkstemp()
    uifile_bytes = util.read_resource(_uiform, pkg_or_mod=pkg_or_mod,
      rsrc_path=rsrc_path).encode()
    with os.fdopen(ui_tempdes, 'w') as fOut:
      fOut.write(uifile_bytes.decode('utf-8'))
      fOut.close()
    if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
      self.engine = QtQml.QQmlApplicationEngine(ui_temppath)
      #self.engine.rootContext().setContextProperty('handler', Hdlr)
      self.rootObject = self.engine.rootObjects()[0]
      self.decl_view = self.rootObject
    else:
      self.decl_view = QtDeclarative.QDeclarativeView(
        QtCore.QUrl.fromLocalFile(ui_temppath))
      self.decl_view.setResizeMode(
        QtDeclarative.QDeclarativeView.SizeRootObjectToView)
      #self.engine.rootContext().setContextProperty('handler', Hdlr)
      self.rootObject = self.decl_view.rootObject()
      self.engine = self.decl_view.engine()
    
    #[self.button1, self.entry1, self.textview1, self.simplebutton1,
    #  self.simpleentry1] = map(lambda nm: self.rootObject.findChild(
    #  QtCore.QObject, nm), ['button1', 'entry1', 'textview1',
    #  'simplebutton1', 'simpleentry1'])
    for name in ['button1', 'entry1', 'textview1', 'simplebutton1',
        'simpleentry1']:
      self.widgets[name] = self.rootObject.findChild(QtCore.QObject, name)
    os.unlink(ui_temppath)

  def update(self, data):
    self._data = data
    #self.rootObject.textview1_updateMessage(self.data)
    self.widgets['textview1'].setProperty('text', self.data)

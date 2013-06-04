# -*- coding: utf-8 -*-
'''Qt interface builder Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
  #from PySide2 import QtCore, QtGui, QtWidgets
  #from PySide2.QtUiTools import QUiLoader
  #from PySide2.QtWidgets import (QWidget, QBoxLayout, QLabel, QPushButton,
  #  QPlainTextEdit, QLineEdit)
  from PyQt5 import sip, uic, Qt, QtCore, QtGui, QtWidgets
  from PyQt5.QtWidgets import (QWidget, QBoxLayout, QLabel, QPushButton,
    QPlainTextEdit, QLineEdit)
  sip.setapi('QVariant', 2)
  klass = QtWidgets.QStackedWidget
  QApplication = QtWidgets.QApplication
else:
  #from PySide import QtCore, QtGui
  #from PySide.QtUiTools import QUiLoader
  #from PySide.QtGui import (QWidget, QBoxLayout, QLabel, QPushButton,
  #  QPlainTextEdit, QLineEdit)
  from PyQt4 import uic, Qt, QtCore, QtGui
  from PyQt4.QtGui import (QWidget, QBoxLayout, QLabel, QPushButton,
    QPlainTextEdit, QLineEdit)
  import sip
  sip.setapi('QVariant', 2)
  klass = QtGui.QStackedWidget
  QApplication = QtGui.QApplication

_uiform = 'qt/helloForm-qt.ui'

__all__ = ['HelloView', 'Qt', 'QtCore', 'QApplication']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(klass, observer.Observer):
  '''Description:: '''

  def __init__(self, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''
    import io

    klass.__init__(self, None)
    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.widgets = {}
    uic.loadUi(io.StringIO(util.read_resource(_uiform, pkg_or_mod=pkg_or_mod,
      rsrc_path=rsrc_path)), self)
    #loader = QUiLoader()
    #main = loader.load(io.StringIO(util.read_resource(_uiform,
    #  pkg_or_mod=pkg_or_mod, rsrc_path=rsrc_path)), self)
    for widgetType, name in [(QWidget, 'form1'), (QWidget, 'dialog1'), 
        (QPushButton, 'button1'), (QPlainTextEdit, 'textview1'), 
        (QLineEdit, 'entry1')]:
      self.widgets[name] = self.findChild(widgetType, name)

  def update(self, data):
    self._data = data
    self.widgets['textview1'].setPlainText(self.data)

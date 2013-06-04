#!/usr/bin/env python -t

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
from future.builtins import (ascii, filter, hex, map, oct, zip, str)

os.environ['QT_QUICK_BACKEND'] = os.environ.get('QT_QUICK_BACKEND', 'software')

if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
  from PySide2 import QtCore, QtGui, QtWidgets, QtQml
  Slot = QtCore.Slot
  #from PyQt5 import sip, Qt, QtCore, QtWidgets, QtQml
  #Slot = QtCore.pyqtSlot
  #sip.setapi('QVariant', 2)
  QApplication = QtWidgets.QApplication
  _uiform = 'qt/helloForm-qt5.qml'
else:
  from PySide import QtCore, QtGui, QtQml
  Slot = QtCore.Slot
  #from PyQt4 import Qt, QtCore, QtGui, QtDeclarative
  #Slot = QtCore.pyqtSlot
  #import sip
  #sip.setapi('QVariant', 2)
  QApplication = QtGui.QApplication
  _uiform = 'qt/helloForm-qt4.qml'

def userifc_version():
  import platform

  return "(Python {0}) Qt {1}".format(platform.python_version(),
    QtCore.qVersion())
  #return "(Python {0}) Qt {1}".format(platform.python_version(),
  #  Qt.QT_VERSION_STR)

class Handler(QtCore.QObject):
  def __init__(self, parent):
    super(QtCore.QObject, self).__init__()
    self.view1 = parent
  
  @Slot()
  def on_button1_clicked(self):
    '''Callback on button1 clicked'''
    
    self.view1.widgets['simplebutton1'].setProperty('opacity', 0)
    self.view1.widgets['entry1'].setProperty('text', '')
    self.view1.widgets['simpleentry1'].setProperty('opacity', 1)
    self.view1.widgets['entry1'].setProperty('focus', 1)
  
  @Slot()
  def on_entry1_returnPressed(self):
    '''Callback on entry1 returnPressed'''
    
    self.view1.widgets['simpleentry1'].setProperty('opacity', 0)
    self.view1.widgets['simplebutton1'].setProperty('opacity', 1)
    self.view1.widgets['textview1'].setProperty('text', 'Hello, ' +
      self.view1.widgets['entry1'].property('text') + '.')

class HelloQtquickDemo(QtCore.QObject):
  '''Description:: '''

  def __init__(self, parent=None):
    '''Construct object'''
    
    # QtCore.QObject.__init__(self, parent)
    super(HelloQtquickDemo, self).__init__(parent)
    
    self.widgets = {}
    rsrc_path = os.environ.get('RSRC_PATH', 'resources')
    if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
      self.engine = QtQml.QQmlApplicationEngine(rsrc_path + '/' + _uiform)
      #self.engine.rootContext().setContextProperty('handler', Hdlr)
      self.rootObject = self.engine.rootObjects()[0]
      self.decl_view = self.rootObject
    else:
      self.decl_view = QtDeclarative.QDeclarativeView(
        QtCore.QUrl.fromLocalFile(rsrc_path + '/' + _uiform))
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
    
    #self.hdlr = Handler(self)
    #self.engine.rootContext().setContextProperty('handler', self.hdlr)
    self.engine.rootContext().setContextProperty('handler', self)
    self.decl_view.setGeometry(400, 300, 240, 160)
    self.decl_view.show()
  
  @Slot()
  def on_button1_clicked(self):
    '''Callback on button1 clicked'''
    
    self.widgets['simplebutton1'].setProperty('opacity', 0)
    self.widgets['entry1'].setProperty('text', '')
    self.widgets['simpleentry1'].setProperty('opacity', 1)
    self.widgets['entry1'].setProperty('focus', 1)
  
  @Slot()
  def on_entry1_returnPressed(self):
    '''Callback on entry1 returnPressed'''
    
    self.widgets['simpleentry1'].setProperty('opacity', 0)
    self.widgets['simplebutton1'].setProperty('opacity', 1)
    self.widgets['textview1'].setProperty('text', 'Hello, ' +
      self.widgets['entry1'].property('text') + '.')

def main(argv=None):
  app = QApplication([])
  pretext = '{0} GUI\n'.format(userifc_version())
  gui = HelloQtquickDemo()
  gui.widgets['textview1'].setProperty('text', pretext)
  
  app.exec_()
  return 0

if '__main__' == __name__:
  sys.exit(main(sys.argv[1:]))


# (one-time): pip install --user pyside2 pyqt5
# [QT_QUICK_BACKEND=software] python helloqtquickdemo.py

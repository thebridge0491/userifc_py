# -*- coding: utf-8 -*-
'''QtQuick interface Hello-Controller module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from userifc_py.qt.hello_model import HelloModel
from userifc_py.qt.hello_quickformview import QtCore, HelloView, QApplication

if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
  Slot = QtCore.Slot    # PySide2
  #Slot = QtCore.pyqtSlot # PyQt5
else:
  Slot = QtCore.Slot    # PySide
  #Slot = QtCore.pyqtSlot # PyQt4

__all__ = ['HelloController', 'QApplication', 'userifc_version']


#MODULE_LOGGER = logging.getLogger(__name__)

def userifc_version():
  import platform

  return "(Python {0}) Qt {1}".format(platform.python_version(),
    QtCore.qVersion())
  #return "(Python {0}) Qt {1}".format(platform.python_version(),
  #  Qt.QT_VERSION_STR)

class Handler(QtCore.QObject):
  def __init__(self, parent):
    #super(QtCore.QObject, self).__init__()
    super(Handler, self).__init__()
    self.parent = parent
    self.view1 = self.parent.view1
    #self.view1 = parent.view1
    #self.model = parent.model
  
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
    self.parent.model.notifyObservers(
      self.view1.widgets['entry1'].property('text'))

#class HelloController(QtCore.QObject):
class HelloController(object):
  '''Description:: '''

  def __init__(self, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    #super(HelloController, self).__init__(None)

    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._model = HelloModel(greetpath, pkg_or_mod, rsrc_path)
    self._view1 = HelloView(__name__, rsrc_path) # HelloView()
    #self._view2 = HelloView(__name__, rsrc_path) # HelloView()
    
    self.hdlr = Handler(self)
    self.view1.engine.rootContext().setContextProperty('handler', self.hdlr)
    #self.view1.engine.rootContext().setContextProperty('handler', self)
    
    self.model.attachObserver(self.view1) # view[1 .. N]
    self.view1.decl_view.setGeometry(400, 300, 240, 160)
    self.view1.decl_view.show()

  @property
  def model(self):
    return self._model

  #@model.setter
  #def model(self, newmodel):
  #  self._model = newmodel

  @property
  def view1(self):
    return self._view1

  #@view1.setter
  #def view1(self, newview):
  #  self._view1 = newview
  
  ## requires inherit QtCore.QObject
  #@Slot()
  #def on_button1_clicked(self):
  #  '''Callback on button1 clicked'''
  #  
  #  self.view1.widgets['simplebutton1'].setProperty('opacity', 0)
  #  self.view1.widgets['entry1'].setProperty('text', '')
  #  self.view1.widgets['simpleentry1'].setProperty('opacity', 1)
  #  self.view1.widgets['entry1'].setProperty('focus', 1)
  
  ## requires inherit QtCore.QObject
  #@Slot()
  #def on_entry1_returnPressed(self):
  #  '''Callback on entry1 returnPressed'''
  #  
  #  self.view1.widgets['simpleentry1'].setProperty('opacity', 0)
  #  self.view1.widgets['simplebutton1'].setProperty('opacity', 1)
  #  self.model.notifyObservers(self.view1.widgets['entry1'].property('text'))

# -*- coding: utf-8 -*-
'''Qt interface Hello-Controller module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from userifc_py.qt.hello_model import HelloModel
from userifc_py.qt.hello_formview import Qt, QtCore, HelloView, QApplication

if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
  #Slot = QtCore.Slot    # PySide2
  Slot = QtCore.pyqtSlot # PyQt5
else:
  #Slot = QtCore.Slot    # PySide
  Slot = QtCore.pyqtSlot # PyQt4

__all__ = ['HelloController', 'QApplication', 'userifc_version']


#MODULE_LOGGER = logging.getLogger(__name__)

def userifc_version():
  import platform

  return "(Python {0}) Qt {1}".format(platform.python_version(),
    QtCore.qVersion())
  #return "(Python {0}) Qt {1}".format(platform.python_version(),
  #  Qt.QT_VERSION_STR)

class HelloController(object):
  '''Description:: '''

  def __init__(self, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    #super(HelloController, self).__init__(greetpath, pkg_or_mod, rsrc_path)

    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._model = HelloModel(greetpath, pkg_or_mod, rsrc_path)
    self._view1 = HelloView(__name__, rsrc_path) # HelloView()
    #self._view2 = HelloView(__name__, rsrc_path) # HelloView()
    
    ## --- Qt4 old-style signal/slot support ---
    #QtCore.QObject.connect(self, QtCore.SIGNAL("destroyed()"),
    #  self.view1.close)
    #QtCore.QObject.connect(self.view1.widgets['form1'], 
    #  QtCore.SIGNAL("destroyed()"), self.view1.widgets['form1'].close)
    #QtCore.QObject.connect(self.view1.widgets['dialog1'], 
    #  QtCore.SIGNAL("destroyed()"), self.view1.widgets['dialog1'].close)
    #QtCore.QObject.connect(self.view1.widgets['button1'], 
    #  QtCore.SIGNAL('clicked()'), self.on_button1_clicked)
    #QtCore.QObject.connect(self.view1.widgets['entry1'], 
    #  QtCore.SIGNAL('editingFinished()'), self.on_entry1_editingFinished)
    #QtCore.QObject.connect(self.view1.widgets['entry1'], 
    #  QtCore.SIGNAL('returnPressed()'), self.on_entry1_returnPressed)
  
    # --- new-style signal/slot support ---
    self.view1.destroyed.connect(self.view1.close)
    self.view1.widgets['form1'].destroyed.connect(
      self.view1.widgets['form1'].close)
    self.view1.widgets['dialog1'].destroyed.connect(
      self.view1.widgets['dialog1'].close)
    self.view1.widgets['button1'].clicked.connect(self.on_button1_clicked)
    #self.view1.widgets['entry1'].editingFinished.connect(
    #  self.on_entry1_editingFinished)
    self.view1.widgets['entry1'].returnPressed.connect(
      self.on_entry1_returnPressed)
  
    ## --- ??? connect slots by name ??? ---
    #QtCore.QMetaObject.connectSlotsByName(self)
    
    self.model.attachObserver(self.view1) # view[1 .. N]
    self.view1.widgets['dialog1'].hide()
    self.view1.setCurrentIndex(self.view1.indexOf(
      self.view1.widgets['form1']))
    self.view1.show()

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

  #@Slot()
  def on_button1_clicked(self):
    '''Callback on button1 clicked'''
    
    self.view1.show()
    self.view1.setCurrentIndex(self.view1.indexOf(
      self.view1.widgets['dialog1']))
    self.view1.widgets['entry1'].setFocus()
    self.view1.widgets['entry1'].setText('')
  
  ##@Slot()
  #def on_entry1_editingFinished(self):
  #  '''Callback on entry1 editingFinished'''
  #  
  #  self.view1.widgets['textview1'].setPlainText('Hello, ' + 
  #    self.view1.widgets['entry1'].text() + '.')
  
  #@Slot()
  def on_entry1_returnPressed(self):
    '''Callback on entry1 returnPressed'''
    
    self.view1.show()
    self.view1.setCurrentIndex(self.view1.indexOf(
      self.view1.widgets['form1']))
    self.model.notifyObservers(self.view1.widgets['entry1'].text())

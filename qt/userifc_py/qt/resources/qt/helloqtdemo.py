#!/usr/bin/env python -t

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
from future.builtins import (ascii, filter, hex, map, oct, zip, str)

if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
  #from PySide2 import QtCore, QtGui, QtWidgets
  #Slot = QtCore.Slot
  #from PySide2.QtUiTools import QUiLoader
  #from PySide2.QtWidgets import (QWidget, QBoxLayout, QLabel, QPushButton,
  #  QPlainTextEdit, QLineEdit)
  from PyQt5 import sip, uic, Qt, QtCore, QtGui, QtWidgets
  Slot = QtCore.pyqtSlot
  from PyQt5.QtWidgets import (QWidget, QBoxLayout, QLabel, QPushButton,
    QPlainTextEdit, QLineEdit)
  sip.setapi('QVariant', 2)
  klass = QtWidgets.QStackedWidget
  QApplication = QtWidgets.QApplication
else:
  #from PySide import QtCore, QtGui
  #Slot = QtCore.Slot
  #from PySide.QtUiTools import QUiLoader
  #from PySide.QtGui import (QWidget, QBoxLayout, QLabel, QPushButton,
  #  QPlainTextEdit, QLineEdit)
  from PyQt4 import uic, Qt, QtCore, QtGui
  Slot = QtCore.pyqtSlot
  from PyQt4.QtGui import (QWidget, QBoxLayout, QLabel, QPushButton,
    QPlainTextEdit, QLineEdit)
  import sip
  sip.setapi('QVariant', 2)
  klass = QtGui.QStackedWidget
  QApplication = QtGui.QApplication

_uiform = 'qt/helloForm-qt.ui'

def userifc_version():
  import platform

  return "(Python {0}) Qt {1}".format(platform.python_version(),
    QtCore.qVersion())
  #return "(Python {0}) Qt {1}".format(platform.python_version(),
  #  Qt.QT_VERSION_STR)

class HelloQtDemo(klass):
  '''Description:: '''

  def __init__(self, parent=None):
    '''Construct object'''
    
    # klass.__init__(self, parent)
    super(HelloQtDemo, self).__init__(parent)
    
    self.widgets = {}
    
    #self.widgets['form1'] = QWidget()
    #self.widgets['verticalLayout'] = QBoxLayout(
    #  QBoxLayout.Direction.TopToBottom, self.widgets['form1'])
    #self.widgets['label1'] = QLabel('label', self.widgets['form1'])
    #self.widgets['button1'] = QPushButton('button', self.widgets['form1'])
    #self.widgets['textview1'] = QPlainTextEdit(self.widgets['form1'])
    #self.widgets['dialog1'] = QWidget()
    #self.widgets['verticalLayout_2'] = QBoxLayout(
    #  QBoxLayout.Direction.TopToBottom, self.widgets['dialog1'])
    #self.widgets['entry1'] = QLineEdit(self.widgets['dialog1'])
    #for widget in [self.widgets['label1'], self.widgets['button1'], 
    #    self.widgets['textview1']]:
    #  self.widgets['verticalLayout'].addWidget(widget)
    #self.widgets['verticalLayout_2'].addWidget(self.widgets['entry1'])
    #self.addWidget(self.widgets['form1'])
    #self.addWidget(self.widgets['dialog1'])
    
    rsrc_path = os.environ.get('RSRC_PATH', 'resources')
    uic.loadUi(rsrc_path + '/' + _uiform, self)
    #loader = QUiLoader()
    #main = loader.load(rsrc_path + '/' + _uiform, self)
    for widgetType, name in [(QWidget, 'form1'), (QWidget, 'dialog1'), 
        (QPushButton, 'button1'), (QPlainTextEdit, 'textview1'), 
        (QLineEdit, 'entry1')]:
      self.widgets[name] = self.findChild(widgetType, name)

    ## --- Qt4 old-style signal/slot support ---
    #QtCore.QObject.connect(self, QtCore.SIGNAL("destroyed()"), self.close)
    #QtCore.QObject.connect(self.widgets['form1'], 
    #  QtCore.SIGNAL("destroyed()"), self.widgets['form1'].close)
    #QtCore.QObject.connect(self.widgets['dialog1'], 
    #  QtCore.SIGNAL("destroyed()"), self.widgets['dialog1'].close)
    #QtCore.QObject.connect(self.widgets['button1'], 
    #  QtCore.SIGNAL('clicked()'), self.on_button1_clicked)
    #QtCore.QObject.connect(self.widgets['entry1'], 
    #  QtCore.SIGNAL('editingFinished()'), self.on_entry1_editingFinished)
    #QtCore.QObject.connect(self.widgets['entry1'], 
    #  QtCore.SIGNAL('returnPressed()'), self.on_entry1_returnPressed)
  
    # --- new-style signal/slot support ---
    self.destroyed.connect(self.close)
    self.widgets['form1'].destroyed.connect(self.widgets['form1'].close)
    self.widgets['dialog1'].destroyed.connect(self.widgets['dialog1'].close)
    self.widgets['button1'].clicked.connect(self.on_button1_clicked)
    #self.widgets['entry1'].editingFinished.connect(
    #  self.on_entry1_editingFinished)
    self.widgets['entry1'].returnPressed.connect(self.on_entry1_returnPressed)
  
    ## --- ??? connect slots by name ??? ---
    #QtCore.QMetaObject.connectSlotsByName(self)
    
    self.widgets['dialog1'].hide()
    self.setCurrentIndex(self.indexOf(self.widgets['form1']))
    self.show()

  #@Slot()
  def on_button1_clicked(self):
    '''Callback on button1 clicked'''
    
    self.show()
    self.setCurrentIndex(self.indexOf(self.widgets['dialog1']))
    self.widgets['entry1'].setFocus()
    self.widgets['entry1'].setText('')
  
  #@Slot()
  def on_entry1_returnPressed(self):
    '''Callback on entry1 returnPressed'''
    
    self.show()
    self.setCurrentIndex(self.indexOf(self.widgets['form1']))
    self.widgets['textview1'].setPlainText('Hello, ' + 
      self.widgets['entry1'].text() + '.')

def main(argv=None):
  app = QApplication([])
  pretext = '{0} GUI\n'.format(userifc_version())
  gui = HelloQtDemo()
  gui.widgets['textview1'].setPlainText(pretext)
  
  app.exec_()
  return 0

if '__main__' == __name__:
  sys.exit(main(sys.argv[1:]))


# (one-time): pip install --user pyside2 pyqt5
# python helloqtdemo.py

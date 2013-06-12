# -*- coding: utf-8 -*-
'''Swing interface Hello-Controller module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')

from java.lang import System, Runnable
from java.awt import EventQueue
from java.awt.event import WindowAdapter #, ActionEvent, ActionListener
from javax.swing import JFrame

from userifc_py.swing.hello_model import HelloModel
from userifc_py.swing.hello_formview import HelloView

__all__ = ['HelloController', 'userifc_version', 'App']


#MODULE_LOGGER = logging.getLogger(__name__)

def userifc_version():
  import platform

  return "(Jython {0}) Java {1} Swing".format(platform.python_version(),
    System.getProperty("java.version"))

class HelloController(object):
  '''Description:: '''

  def __init__(self, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    #super(HelloController, self).__init__(greetpath, pkg_or_mod, rsrc_path)

    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._model = HelloModel(greetpath, pkg_or_mod, rsrc_path)
    self._view1 = HelloView() # HelloView()
    #self._view2 = HelloView() # HelloView()

    self.view1.widgets['frame1'].setDefaultCloseOperation(
      JFrame.EXIT_ON_CLOSE)
    self.view1.widgets['dialog1'].addWindowListener(self.Dialog1Listener())
    #self.view1.widgets['button1'].addActionListener(self.Button1Listener())
    #self.view1.widgets['entry1'].addActionListener(self.Entry1Listener())
    self.view1.widgets['button1'].addActionListener(self.onButton1Action)
    self.view1.widgets['entry1'].addActionListener(self.onEntry1Action)

    self.model.attachObserver(self.view1) # view[1 .. N]
    self.view1.widgets['frame1'].visible = True

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

  class Dialog1Listener(WindowAdapter):
    '''Window adapter/listener for dialog1'''
    
    def windowClosing(self, event):
      sys.exit(0)
  
#  class Button1Listener(ActionListener):
#    '''Action listener for button1'''
#    
#    def actionPerformed(self, event):
#      HelloController.view1.widgets['frame1'].visible = False
#      HelloController.view1.widgets['dialog1'].visible = True
#      HelloController.view1.widgets['entry1'].text = ""

#  class Entry1Listener(ActionListener):
#    '''Action listener for entry1'''
#    
#    def actionPerformed(self, event):
#      HelloController.view1.widgets['dialog1'].visible = False
#      HelloController.view1.widgets['frame1'].visible = True
#      HelloController.model.notifyObservers(
#        HelloController.view1.widgets['entry1'].text)
  
  def onButton1Action(self, event):
    '''Action listener for button1'''
    
    self.view1.widgets['frame1'].visible = False
    self.view1.widgets['dialog1'].visible = True
    self.view1.widgets['entry1'].text = ""

  def onEntry1Action(self, event):
    '''Action listener for entry1'''
    
    self.view1.widgets['dialog1'].visible = False
    self.view1.widgets['frame1'].visible = True
    self.model.notifyObservers(self.view1.widgets['entry1'].text)

class App(Runnable):
  def __init__(self, pretext, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    self.pretext, self.greetpath = pretext, greetpath
    self.pkg_or_mod, self.rsrc_path = pkg_or_mod, rsrc_path
  
  def run(self):
    gui = HelloController(self.greetpath, self.pkg_or_mod, self.rsrc_path)
    gui.view1.widgets['textview1'].text = self.pretext

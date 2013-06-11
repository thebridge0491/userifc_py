# -*- coding: utf-8 -*-
'''wxWidgets interface Hello-Controller module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from userifc_py.wxwidgets.hello_model import HelloModel
from userifc_py.wxwidgets.hello_formview import wx, HelloView

__all__ = ['wx', 'HelloController', 'userifc_version']


#MODULE_LOGGER = logging.getLogger(__name__)

def userifc_version():
  import platform

  return "(Python {0}) WxGtk {1}".format(platform.python_version(), 
    wx.version())

class HelloController(object):
  '''Description:: '''

  def __init__(self, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    #super(HelloController, self).__init__(greetpath, pkg_or_mod, rsrc_path)
    self.app = wx.App(False)

    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._model = HelloModel(greetpath, pkg_or_mod, rsrc_path)
    self._view1 = HelloView(self.app, __name__, rsrc_path) # HelloView(self.app)
    #self._view2 = HelloView(self.app,__name__, rsrc_path) # HelloView(self.app)
    
    # connect signal callbacks
    self.view1.widgets['frame1'].Bind(wx.EVT_CLOSE, self.on_frame1_closed, 
      self.view1.widgets['frame1'])
    self.view1.widgets['dialog1'].Bind(wx.EVT_CLOSE, self.on_dialog1_closed, 
      self.view1.widgets['dialog1'])
    self.view1.widgets['button1'].Bind(wx.EVT_BUTTON, self.on_button1_clicked, 
      self.view1.widgets['button1'])
    self.view1.widgets['entry1'].Bind(wx.EVT_TEXT, self.on_entry1_textChanged, 
      self.view1.widgets['entry1'])
    self.view1.widgets['entry1'].Bind(wx.EVT_TEXT_ENTER, 
      self.on_entry1_returnPressed, self.view1.widgets['entry1'])

    self.model.attachObserver(self.view1) # view[1 .. N]
    self.app.SetTopWindow(self.view1.widgets['frame1'])
    self.view1.widgets['frame1'].Show(True)

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

  def on_frame1_closed(self, frame1, callback_data=None):
    '''Callback for frame1 closed'''
    
    wx.Exit()
  
  def on_dialog1_closed(self, dialog1, callback_data=None):
    '''Callback for dialog1 closed'''
    
    self.view1.widgets['frame1'].Close()
  
  def on_button1_clicked(self, button1, callback_data=None):
    '''Callback for button1 clicked'''
    
    self.view1.widgets['frame1'].Hide()
    self.view1.widgets['dialog1'].Show(True)
    self.view1.widgets['entry1'].SetFocus()
    self.view1.widgets['entry1'].SetValue('')
  
  def on_entry1_textChanged(self, entry1, callback_data=None):
    '''Callback for entry1 textChanged'''
    
    
  
  def on_entry1_returnPressed(self, entry1, callback_data=None):
    '''Callback for entry1 returnPressed'''
    
    self.model.notifyObservers(self.view1.widgets['entry1'].Value)
    self.view1.widgets['dialog1'].Hide()
    self.view1.widgets['frame1'].Show(True)

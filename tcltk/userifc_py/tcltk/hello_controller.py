# -*- coding: utf-8 -*-
'''Tcl/Tk interface Hello-Controller module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from userifc_py.tcltk.hello_model import HelloModel
from userifc_py.tcltk.hello_view import tk, HelloView

__all__ = ['tk', 'HelloController', 'userifc_version']


#MODULE_LOGGER = logging.getLogger(__name__)

def userifc_version():
  import platform

  return "(Python {0}) Tk {1}".format(platform.python_version(),
    tk.TkVersion)

class HelloController(object):
  '''Description:: '''

  def __init__(self, app, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    #super(HelloController, self).__init__(greetpath, pkg_or_mod, rsrc_path)

    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.app = app
    self._model = HelloModel(greetpath, pkg_or_mod, rsrc_path)
    self._view1 = HelloView(self.app)
    #self._view2 = HelloView()
    
    self.view1.widgets['dialog1'].bind('<Destroy>', self.dialog1_destroyed_cb)
    self.view1.widgets['button1'].bind('<Button>', self.button1_clicked_cb)
    self.view1.widgets['txt1'].trace('w', self.entry1_textChanged_cb)
    self.view1.widgets['entry1'].bind('<Return>',
      self.entry1_returnPressed_cb)

    self.model.attachObserver(self.view1) # view[1 .. N]
    self.app.title('frame1')
    self.view1.widgets['frame1'].lift()

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

  def dialog1_destroyed_cb(self, dialog1, callback_data=None):
    '''Callback for dialog1 destroyed'''

    self.app.quit()

  def button1_clicked_cb(self, button1, callback_data=None):
    '''Callback for button1 clicked'''
    
    #try:
    #  import tkSimpleDialog as simpledialog
    #except ImportError as exc:
    #  print(repr(exc))
    #  import tkinter.simpledialog as simpledialog
    #data = simpledialog.askstring('dialog1', '', 
    #  parent=self.view1.widgets['frame1'])

    self.view1.widgets['dialog1'].deiconify()
    self.app.withdraw()
    self.view1.widgets['entry1'].focus_set()
    self.view1.widgets['entry1'].delete(0, tk.END)

  def entry1_textChanged_cb(self, entry1, extra, callback_data=None):
    '''Callback for entry1 textChanged'''

    self.view1.widgets['textview1'].delete(1.0, tk.END)

  def entry1_returnPressed_cb(self, entry1, callback_data=None):
    '''Callback for entry1 returnPressed'''

    self.app.deiconify()
    self.view1.widgets['dialog1'].withdraw()
    self.model.notifyObservers(self.view1.widgets['entry1'].get())

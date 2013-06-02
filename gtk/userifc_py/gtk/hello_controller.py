# -*- coding: utf-8 -*-
'''Gtk interface Hello-Controller module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from userifc_py.gtk.hello_model import HelloModel
from userifc_py.gtk.hello_formview import Gtk, HelloView

__all__ = ['Gtk', 'HelloController', 'userifc_version']


#MODULE_LOGGER = logging.getLogger(__name__)

def userifc_version():
  import platform

  try:    # version >2.99
    major_version, minor_version = Gtk.MAJOR_VERSION, Gtk.MINOR_VERSION
  except: # version <2.99
    major_version, minor_version, micro_version = Gtk.gtk_version
  return "(Python {0}) Gtk+ {1}.{2}".format(platform.python_version(),
    major_version, minor_version)

class HelloController(object):
  '''Description:: '''

  def __init__(self, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    #super(HelloController, self).__init__(greetpath, pkg_or_mod, rsrc_path)

    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._model = HelloModel(greetpath, pkg_or_mod, rsrc_path)
    self._view1 = HelloView(__name__, rsrc_path) # HelloView()
    #self._view2 = HelloView(__name__, rsrc_path) # HelloView()

    try:
      self.view1.connect_signals(self)
    except:
      [window1, button1, dialog1, entry1] = map(self.view1.widgets.get,
        ['window1', 'button1', 'dialog1', 'entry1'])
      window1.connect('destroy', self.window1_destroy_cb)
      dialog1.connect('destroy', self.dialog1_destroy_cb)
      dialog1.connect('response', self.dialog1_response_cb)
      button1.connect('clicked', self.button1_clicked_cb)
      entry1.connect('activate', self.entry1_activate_cb)

    self.model.attachObserver(self.view1) # view[1 .. N]
    self.view1.widgets['window1'].set_default_size(200, 160)
    self.view1.widgets['window1'].show_all()

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

  def window1_destroy_cb(self, window1, callback_data=None):
    '''Callback for window1 destroy'''

    func_name = inspect.stack()[0][3]
    self.logger.debug(func_name + '()')
    Gtk.main_quit(callback_data)

  def dialog1_destroy_cb(self, dialog1, callback_data=None):
    '''Callback for dialog1 destroy'''

    func_name = inspect.stack()[0][3]
    self.logger.debug(func_name + '()')
    self.view1.widgets['window1'].destroy()

  def dialog1_response_cb(self, dialog1, callback_data=None):
    '''Callback for dialog1 response'''

    func_name = inspect.stack()[0][3]
    self.logger.debug(func_name + '()')
    self.view1.widgets['entry1'].activate()
    dialog1.hide()

  def button1_clicked_cb(self, button1, callback_data=None):
    '''Callback for button1 clicked'''

    func_name = inspect.stack()[0][3]
    self.logger.debug(func_name + '()')
    self.view1.widgets['textview1'].show()
    self.view1.widgets['dialog1'].show_all()
    self.view1.widgets['entry1'].set_text('')

  def entry1_activate_cb(self, entry1, callback_data=None):
    '''Callback for entry1 activate'''

    func_name = inspect.stack()[0][3]
    self.logger.debug(func_name + '()')
    self.view1.widgets['dialog1'].hide()
    self.model.notifyObservers(entry1.get_text())

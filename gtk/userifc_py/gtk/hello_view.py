# -*- coding: utf-8 -*-
'''Gtk interface (hand-coded) Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

if '2' == os.environ.get('GTK_MAJOR_VERSION', 'LATEST'):
  import pygtk
  pygtk.require('2.0')
  import gtk as Gtk
else:
  import gi
  gi.require_version('Gtk', '3.0')
  from gi.repository import Gtk

__all__ = ['HelloView', 'Gtk']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(Gtk.Window, observer.Observer):
  '''Description:: '''

  def __init__(self):
    '''Construct object'''

    Gtk.Window.__init__(self)
    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.widgets = {}
    self.widgets['frame1'] = Gtk.Frame()
    self.widgets['vbox1'] = Gtk.VBox(spacing=10)
    self.widgets['label1'] = Gtk.Label('label')
    self.widgets['button1'] = Gtk.Button(label='button')
    self.widgets['textview1'] = Gtk.TextView()
    self.widgets['dialog1'] = Gtk.Dialog()
    self.widgets['entry1'] = Gtk.Entry()

    for widget in map(self.widgets.get, ['label1', 'button1', 'textview1']):
      self.widgets['vbox1'].pack_start(widget, True, True, 0)
    #self.widgets['dialog1'].get_content_area().pack_start(
    #  self.widgets['entry1'], False, False, 0)
    self.widgets['dialog1'].vbox.pack_start(self.widgets['entry1'],
      False, False, 0)
    self.widgets['frame1'].add(self.widgets['vbox1'])
    self.add(self.widgets['frame1'])

  def update(self, data):
    self._data = data
    self.widgets['textview1'].get_buffer().set_text(self.data)

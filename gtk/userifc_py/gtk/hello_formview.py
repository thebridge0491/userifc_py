# -*- coding: utf-8 -*-
'''Gtk interface builder Hello-View module (for Model-View-Controller)

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
  _uiform = 'gtk/helloForm-gtk2.glade'
else:
  import gi
  gi.require_version('Gtk', '3.0')
  from gi.repository import Gtk
  _uiform = 'gtk/helloForm-gtk3.glade'

__all__ = ['HelloView', 'Gtk']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(Gtk.Builder, observer.Observer):
  '''Description:: '''

  def __init__(self, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    Gtk.Builder.__init__(self)
    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.widgets = {}
    self.add_from_string(util.read_resource(_uiform, pkg_or_mod=pkg_or_mod,
      rsrc_path=rsrc_path))
    for name in ['window1', 'dialog1', 'button1', 'textview1', 'entry1']:
    	self.widgets[name] = self.get_object(name)

  def update(self, data):
    self._data = data
    self.widgets['textview1'].get_buffer().set_text(self.data)

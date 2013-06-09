# -*- coding: utf-8 -*-
'''Tcl/Tk interface (hand-coded) Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

try:
  import tkinter as tk
except ImportError as exc:
  print(repr(exc))
  import Tkinter as tk

__all__ = ['HelloView', 'tk']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(tk.Frame, observer.Observer):
  '''Description:: '''

  def __init__(self, app=None):
    '''Construct object'''

    tk.Frame.__init__(self, app)
    observer.Observer.__init__(self)
    #super(HelloView, self).__init__(app)

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.app, self.widgets = app, {}
    self.widgets['frame1'] = tk.Frame(self.app)
    self.widgets['label1'] = tk.Label(self.widgets['frame1'], text='label1')
    self.widgets['button1'] = tk.Button(self.widgets['frame1'], 
      text='button1')
    self.widgets['textview1'] = tk.Text(self.widgets['frame1'], height=3, 
      width=30)
    self.widgets['frame1'].pack()
    
    for widget in map(self.widgets.get, ['label1', 'button1', 'textview1']):
      widget.pack()
    
    self.widgets['dialog1'] = tk.Toplevel()
    self.widgets['dialog1'].title('dialog1')
    self.widgets['frameDialog1'] = tk.Frame(self.widgets['dialog1'])
    self.widgets['txt1'] = tk.StringVar()
    self.widgets['entry1'] = tk.Entry(master=self.widgets['frameDialog1'],
      width=25, textvariable=self.widgets['txt1'])
    self.widgets['entry1'].pack()
    self.widgets['frameDialog1'].pack()
    self.widgets['dialog1'].withdraw()

  def update(self, data):
    self._data = data
    self.widgets['textview1'].delete(1.0, tk.END)
    self.widgets['textview1'].insert(tk.INSERT, self.data)

# -*- coding: utf-8 -*-
'''wxWidgets interface (hand-coded) Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

import wx

__all__ = ['HelloView', 'wx']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(observer.Observer):
  '''Description:: '''

  def __init__(self, app):
    '''Construct object'''

    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.app, self.widgets = app, {}
    self.widgets['frame1'] = wx.Frame(None, title='frame1', name='frame1',
      style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, size=wx.Size(219, 174))
    self.widgets['label1'] = wx.StaticText(self.widgets['frame1'], wx.ID_ANY,
      'label1', style=wx.ALIGN_CENTER)
    self.widgets['button1'] = wx.Button(self.widgets['frame1'], wx.ID_ANY,
      'button1')
    self.widgets['textview1'] = wx.TextCtrl(self.widgets['frame1'], wx.ID_ANY,
      '', style=wx.TE_MULTILINE | wx.TE_WORDWRAP, size=wx.Size(160, 80))
    self.widgets['dialog1'] = wx.Dialog(None, title='dialog1',
      style=wx.DEFAULT_DIALOG_STYLE, size=wx.Size(169, 73))
    self.widgets['entry1'] = wx.TextCtrl(self.widgets['dialog1'], wx.ID_ANY,
      '', style=wx.TE_PROCESS_ENTER)
    self.widgets['frame1'].SetSizer(wx.BoxSizer(wx.VERTICAL))
    self.widgets['dialog1'].SetSizer(wx.BoxSizer(wx.VERTICAL))
    self.widgets['vbox1'] = self.widgets['frame1'].GetSizer()
    self.widgets['dialog_vbox1'] = self.widgets['dialog1'].GetSizer()
    for widget in map(self.widgets.get, ['label1', 'button1', 'textview1']):
      self.widgets['vbox1'].Add(widget, 0, wx.ALIGN_CENTER, 0)
    self.widgets['dialog_vbox1'].Add(self.widgets['entry1'], 0,
      wx.ALIGN_CENTER, 0)
    self.widgets['frame1'].Layout()
    self.widgets['dialog1'].Layout()

  def update(self, data):
    self._data = data
    self.widgets['textview1'].SetValue(self.data)

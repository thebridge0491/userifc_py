# -*- coding: utf-8 -*-
'''wxWidgets interface builder Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

import wx, wx.xrc

_uiform = 'wxwidgets/helloForm-wxwidgets.xrc'

__all__ = ['HelloView', 'wx']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(observer.Observer):
  '''Description:: '''

  def __init__(self, app, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.app, self.widgets = app, {}
    self.res = wx.xrc.EmptyXmlResource()
    #self.res.LoadFile(rsrc_path + '/' + _uiform)
    #self.res = wx.xrc.XmlResource(rsrc_path + '/' + _uiform)
    self.res.LoadFromString(util.read_resource(_uiform, pkg_or_mod=pkg_or_mod,
      rsrc_path=rsrc_path).encode())
    self.widgets['frame1'] = self.res.LoadFrame(None, 'frame1')
    self.widgets['label1'] = wx.xrc.XRCCTRL(self.widgets['frame1'], 'label1')
    self.widgets['button1'] = wx.xrc.XRCCTRL(self.widgets['frame1'], 
      'button1')
    self.widgets['textview1'] = wx.xrc.XRCCTRL(self.widgets['frame1'],
      'textview1')
    self.widgets['dialog1'] = self.res.LoadDialog(None, 'dialog1')
    self.widgets['entry1'] = wx.xrc.XRCCTRL(self.widgets['dialog1'], 'entry1')

  def update(self, data):
    self._data = data
    self.widgets['textview1'].SetValue(self.data)

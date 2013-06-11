#!/usr/bin/env python -t

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
from future.builtins import (ascii, filter, hex, map, oct, zip, str)

import wx, wx.xrc

_uiform = 'wxwidgets/helloForm-wxwidgets.xrc'

def userifc_version():
  import platform

  return "(Python {0}) WxGtk {1}".format(platform.python_version(),
    wx.version())

class HelloWxwidgetsDemo(object):
  '''Description:: '''

  def __init__(self):
    '''Construct object'''

    self.app = wx.App(False)
    self.widgets = {}
    
    #self.widgets['frame1'] = wx.Frame(None, title='frame1', name='frame1',
    #  style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, size=wx.Size(219, 174))
    #self.widgets['label1'] = wx.StaticText(self.widgets['frame1'], wx.ID_ANY,
    #  'label1', style=wx.ALIGN_CENTER)
    #self.widgets['button1'] = wx.Button(self.widgets['frame1'], wx.ID_ANY,
    #  'button1')
    #self.widgets['textview1'] = wx.TextCtrl(self.widgets['frame1'], wx.ID_ANY,
    #  '', style=wx.TE_MULTILINE | wx.TE_WORDWRAP, size=wx.Size(160, 80))
    #self.widgets['dialog1'] = wx.Dialog(None, title='dialog1',
    #  style=wx.DEFAULT_DIALOG_STYLE, size=wx.Size(169, 73))
    #self.widgets['entry1'] = wx.TextCtrl(self.widgets['dialog1'], wx.ID_ANY,
    #  '', style=wx.TE_PROCESS_ENTER)
    #self.widgets['frame1'].SetSizer(wx.BoxSizer(wx.VERTICAL))
    #self.widgets['dialog1'].SetSizer(wx.BoxSizer(wx.VERTICAL))
    #self.widgets['vbox1'] = self.widgets['frame1'].GetSizer()
    #self.widgets['dialog_vbox1'] = self.widgets['dialog1'].GetSizer()
    #for widget in map(self.widgets.get, ['label1', 'button1', 'textview1']):
    #  self.widgets['vbox1'].Add(widget, 0, wx.ALIGN_CENTER, 0)
    #self.widgets['dialog_vbox1'].Add(self.widgets['entry1'], 0,
    #  wx.ALIGN_CENTER, 0)
    #self.widgets['frame1'].Layout()
    #self.widgets['dialog1'].Layout()
    
    rsrc_path = os.environ.get('RSRC_PATH', 'resources')
    #res = wx.xrc.XmlResource(rsrc_path + '/' + _uiform)
    res = wx.xrc.EmptyXmlResource()
    res.LoadFile(rsrc_path + '/' + _uiform)
    self.widgets['frame1'] = res.LoadFrame(None, 'frame1')
    self.widgets['label1'] = wx.xrc.XRCCTRL(self.widgets['frame1'], 'label1')
    self.widgets['button1'] = wx.xrc.XRCCTRL(self.widgets['frame1'], 
      'button1')
    self.widgets['textview1'] = wx.xrc.XRCCTRL(self.widgets['frame1'],
      'textview1')
    self.widgets['dialog1'] = res.LoadDialog(None, 'dialog1')
    self.widgets['entry1'] = wx.xrc.XRCCTRL(self.widgets['dialog1'], 'entry1')
    
    # connect signal callbacks
    self.widgets['frame1'].Bind(wx.EVT_CLOSE, self.on_frame1_closed, 
      self.widgets['frame1'])
    self.widgets['dialog1'].Bind(wx.EVT_CLOSE, self.on_dialog1_closed, 
      self.widgets['dialog1'])
    self.widgets['button1'].Bind(wx.EVT_BUTTON, self.on_button1_clicked, 
      self.widgets['button1'])
    self.widgets['entry1'].Bind(wx.EVT_TEXT, self.on_entry1_textChanged, 
      self.widgets['entry1'])
    self.widgets['entry1'].Bind(wx.EVT_TEXT_ENTER, 
      self.on_entry1_returnPressed, self.widgets['entry1'])
    
    self.app.SetTopWindow(self.widgets['frame1'])
    self.widgets['frame1'].Show(True)

  def on_frame1_closed(self, frame1, callback_data=None):
    '''Callback for frame1 closed'''
    
    wx.Exit()
  
  def on_dialog1_closed(self, dialog1, callback_data=None):
    '''Callback for dialog1 closed'''
    
    self.widgets['frame1'].Close()
  
  def on_button1_clicked(self, button1, callback_data=None):
    '''Callback for button1 clicked'''
    
    self.widgets['frame1'].Hide()
    self.widgets['dialog1'].Show(True)
    self.widgets['entry1'].SetFocus()
    self.widgets['entry1'].SetValue('')
  
  def on_entry1_textChanged(self, entry1, callback_data=None):
    '''Callback for entry1 textChanged'''
    
    
  
  def on_entry1_returnPressed(self, entry1, callback_data=None):
    '''Callback for entry1 returnPressed'''
    
    self.widgets['textview1'].SetValue("Hello, " + 
      self.widgets['entry1'].Value + ".")
    self.widgets['dialog1'].Hide()
    self.widgets['frame1'].Show(True)

def main(argv=None):
  pretext = '{0} GUI\n'.format(userifc_version())
  gui = HelloWxwidgetsDemo()
  gui.widgets['textview1'].SetValue(pretext)
  
  gui.app.MainLoop()
  return 0

if '__main__' == __name__:
  sys.exit(main(sys.argv[1:]))


# (one-time): pip install --user wxpython
# python hellowxwidgetsdemo.py

# -*- coding: utf-8 -*-
'''Test cases for Model, View, and Controller.'''
from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import unittest
#from future.builtins import (ascii, filter, hex, map, oct, zip, range)

from userifc_py.wxwidgets.hello_controller import wx, HelloController

def setUpModule():
  '''Set up (module-level) test fixtures, if any.'''
  print('Setup module: {0}'.format(__name__))

def tearDownModule():
  '''Tear down (module-level) test fixtures, if any.'''
  print('Teardown module: {0}'.format(__name__))

def refresh_ui(app, delay=0):
  '''Refresh UI by cycling through all pending events'''
  import time

  while app.HasPendingEvents():
    app.ProcessPendingEvents()
  time.sleep(delay)


class TestViewController(unittest.TestCase):
  userifc = HelloController('greet.txt', 'userifc_py.wxwidgets')
  app = userifc.app
  view1 = userifc.view1
  delay_secs = 3.0

  @classmethod
  def setUpClass(cls):
    #print('Setup class: {0}'.format(cls.__name__))
    pass

  @classmethod
  def tearDownClass(cls):
    #print('\nTeardown class: {0}'.format(cls.__name__))
    pass

  def setUp(self):
    #print('Setup method: {0}'.format(self._testMethodName))
    pass

  def tearDown(self):
    #print('Teardown method: {0}'.format(self.id().split('.')[-1]))
    pass

  def test_main(self):
    self.assertTrue(HelloController)  # use your library here
    self.assertTrue(wx)

  def test_use_ok(self):
    '''Can use HelloController class'''
    self.assertTrue(self.userifc)

  def test_on_button1_clicked(self):
    '''Ensure correct actions on button1 clicked.

    Entry1 text is set to ""
    Dialog1 is shown
    Frame1 is not shown
    '''
    [entry1, dialog1, frame1, button1] = map(self.view1.widgets.get,
      ['entry1', 'dialog1', 'frame1', 'button1'])
    entry1.SetValue('xxxxxx')

    button1.ProcessEvent(wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED,
      button1.GetId()))
    refresh_ui(self.userifc.app, self.delay_secs)
    self.assertTrue(dialog1.IsShown() and not frame1.IsShown())
    self.assertEqual(entry1.Value, '')

  def test_on_entry1_textChanged(self):
    '''Ensure correct actions on entry1 textChanged'''

    dialog1 = self.view1.widgets['dialog1']
    entry1 = self.view1.widgets['entry1']
    dialog1.Show()

    entry1.ProcessEvent(wx.CommandEvent(wx.wxEVT_COMMAND_TEXT_UPDATED,
      entry1.GetId()))
    refresh_ui(self.userifc.app, self.delay_secs)
    self.assertTrue(dialog1.IsShown())

  def test_on_entry1_returnPressed(self):
    '''Ensure correct actions on entry1 returnPressed'''

    [entry1, dialog1, textview1] = [self.view1.widgets.get(x) for x in
      ['entry1', 'dialog1', 'textview1']]
    dialog1.Show()
    entry1.SetValue('John Doe')

    entry1.ProcessEvent(wx.CommandEvent(wx.wxEVT_COMMAND_TEXT_ENTER,
      entry1.GetId()))
    refresh_ui(self.userifc.app, self.delay_secs)
    #self.assertEqual(textview1.Value,
    #  list(self.userifc.model._observers)[0].data)
    self.assertEqual(textview1.Value, self.userifc.view1._data)
    self.assertTrue(not dialog1.IsShown())

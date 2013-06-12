# -*- coding: utf-8 -*-
'''Test cases for Model, View, and Controller.'''
from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import sys, unittest
#from future.builtins import (ascii, filter, hex, map, oct, zip, range)

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')

from userifc_py.swing.hello_controller import HelloController

def setUpModule():
  '''Set up (module-level) test fixtures, if any.'''
  print('Setup module: {0}'.format(__name__))

def tearDownModule():
  '''Tear down (module-level) test fixtures, if any.'''
  print('Teardown module: {0}'.format(__name__))

def refresh_ui(delay=0):
  '''Refresh UI by cycling through all pending events'''
  import time

  time.sleep(delay)


class TestViewController(unittest.TestCase):
  userifc = HelloController('greet.txt', 'userifc_py.swing')
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

  def test_use_ok(self):
    '''Can use HelloController class'''
    self.assertTrue(self.userifc)

  def test_on_button1_action(self):
    '''Ensure correct actions from button1 ActionListener.
    
    Entry1 text is set to ""
    Dialog1 is shown
    Frame1 is not shown
    '''
    
    [entry1, dialog1, frame1, button1] = map(self.view1.widgets.get, 
        ['entry1', 'dialog1', 'frame1', 'button1'])
    entry1.text = 'xxxxxx'
    
    button1.doClick()
    refresh_ui(self.delay_secs)
    self.assertTrue(dialog1.visible and not frame1.visible)
    self.assertEqual(entry1.text, '')

  def test_on_dialog1_windowClosing(self):
    '''Ensure correct actions from dialog1 WindowListener'''
    
    dialog1 = self.view1.widgets['dialog1']
    dialog1.visible = True
    
    dialog1.dispose()
    refresh_ui(self.delay_secs)
    self.assertTrue(not dialog1.visible)

  def test_on_entry1_action(self):
    '''Ensure correct actions from entry1 ActionListener'''
    
    [entry1, dialog1, textview1] = [self.view1.widgets.get(x) for x in 
        ['entry1', 'dialog1', 'textview1']]
    dialog1.visible = True
    entry1.text = 'John Doe'
    
    entry1.postActionEvent()
    refresh_ui(self.delay_secs)
    #self.assertEqual(textview1.text,
    #  list(self.userifc.model._observers)[0].data)
    self.assertEqual(textview1.text, self.userifc.view1._data)
    self.assertTrue(not dialog1.visible)

# -*- coding: utf-8 -*-
'''Test cases for Model, View, and Controller.'''
from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import unittest
#from future.builtins import (ascii, filter, hex, map, oct, zip, range)

from userifc_py.tcltk.hello_controller import tk, HelloController

def setUpModule():
  '''Set up (module-level) test fixtures, if any.'''
  print('Setup module: {0}'.format(__name__))

def tearDownModule():
  '''Tear down (module-level) test fixtures, if any.'''
  print('Teardown module: {0}'.format(__name__))

def refresh_ui(app, delay=0):
  '''Refresh UI by cycling through all pending events'''
  import time

  #while app.dooneevent(tk._tkinter.ALL_EVENTS | tk._tkinter.DONT_WAIT):
  #  pass
  app.update_idletasks()
  app.update()
  time.sleep(delay)


class TestViewController(unittest.TestCase):
  app = tk.Tk()
  userifc = HelloController(app, 'greet.txt', 'userifc_py.tcltk')
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
    self.assertTrue(tk)

  def test_use_ok(self):
    '''Can use HelloController class'''
    self.assertTrue(self.userifc)

  def test_button1_clicked_cb(self):
    '''Ensure correct actions on button1 clicked.
    
    Entry1 text is set to ""
    Dialog1 is shown
    Textview1 is shown
    '''
    [entry1, dialog1, textview1, button1] = map(self.view1.widgets.get, 
        ['entry1', 'dialog1', 'textview1', 'button1'])
    entry1.insert(tk.INSERT, 'xxxxxx')
    
    self.userifc.button1_clicked_cb(button1)
    #button1.event_generate('<Button>')
    #button1.invoke()
    refresh_ui(self.app, self.delay_secs)
    #self.assertTrue(dialog1.winfo_viewable())
    self.assertEqual(entry1.get(), '')

  def test_entry1_textChanged_cb(self):
    '''Ensure correct actions on entry1 textChanged'''
    
    [entry1, dialog1, textview1] = [self.view1.widgets.get(x) for x in 
        ['entry1', 'dialog1', 'textview1']]
    dialog1.deiconify()
    
    self.userifc.entry1_textChanged_cb(entry1, '')
    #entry1.event_generate('<<Change>>')
    refresh_ui(self.app, self.delay_secs)
    self.assertEqual(textview1.get(1.0, tk.END).split('\n')[0], '')

  def test_entry1_returnPressed_cb(self):
    '''Ensure correct actions on entry1 returnPressed'''
    
    [entry1, dialog1, textview1] = [self.view1.widgets.get(x) for x in 
        ['entry1', 'dialog1', 'textview1']]
    dialog1.deiconify()
    entry1.insert(tk.INSERT, 'John Doe')
    
    self.userifc.entry1_returnPressed_cb(entry1)
    #entry1.event_generate('<Return>')
    refresh_ui(self.app, self.delay_secs)
    self.assertEqual(textview1.get(1.0, tk.END).split('\n')[0],
      list(self.userifc.model._observers)[0].data)
    self.assertEqual(textview1.get(1.0, tk.END).split('\n')[0],
      self.userifc.view1._data)
    self.assertTrue(not dialog1.winfo_viewable())

# -*- coding: utf-8 -*-
'''Test cases for Model, View, and Controller.'''
from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import unittest
#from future.builtins import (ascii, filter, hex, map, oct, zip, range)

from userifc_py.curses.hello_controller import curses, HelloController, Keys

def setUpModule():
  '''Set up (module-level) test fixtures, if any.'''
  print('Setup module: {0}'.format(__name__))

def tearDownModule():
  '''Tear down (module-level) test fixtures, if any.'''
  print('Teardown module: {0}'.format(__name__))

def refresh_ui(ctrlr, delay=0):
  '''Refresh UI by cycling through all pending events'''
  import time

  if ctrlr.step_virtualscr():
    curses.doupdate()
  time.sleep(delay)


class TestViewController(unittest.TestCase):
  userifc = HelloController('greet.txt', 'userifc_py.curses')
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
    self.assertTrue(curses)

  def test_use_ok(self):
    '''Can use HelloController class'''
    self.assertTrue(self.userifc)
  
  def test_key_enter_cb(self):
    '''Ensure correct actions on cmd Enter.
  
    Input panel set to top
    Window (input panel) set to ""
    Input panel is visible
    '''
    curses.ungetch(Keys['KEY_ENTER'])
    
    self.view1.panels['input'].top()
    #self.view1.panels['input'].window().addstr(1, 1, 'x' * 20)
    self.view1.panels['input'].window().addstr(1, 1,
      ('x' * 7) + ' Push Enter key ' + ('x' * 7))
    self.view1.panels['input'].window().refresh()
    curses.napms(int(self.delay_secs) * 1000)
    
    refresh_ui(self.userifc, self.delay_secs)
    self.assertTrue(not self.view1.panels['input'].hidden())
    self.view1.panels['input'].window().addstr(1, 1, 'John Doe')
    self.userifc.model.notifyObservers('John Doe')
    #self.assertTrue('John Doe' in 
    #  list(self.userifc.model._observers)[0].data)
    self.assertTrue('John Doe' in self.view1._data)

  def test_key_run_cb(self):
    '''Ensure correct actions on cmd Run.
  
    Output panel set to top
    Output panel is visible
    '''
    curses.ungetch(Keys['KEY_RUN'])
    refresh_ui(self.userifc, self.delay_secs)
    self.assertTrue(not self.view1.panels['output'].hidden())

  def test_key_esc_cb(self):
    '''Ensure correct actions on cmd Exit.
  
    Run loop exits
    '''
    curses.ungetch(Keys['KEY_ESC'])
    self.assertFalse(self.userifc.step_virtualscr())

  def test_key_unmapped_cb(self):
    '''Ensure correct actions on unmapped cmd.
  
    Output panel set to top
    Output panel is visible
    '''
    curses.ungetch(ord('Z'))
    refresh_ui(self.userifc, self.delay_secs)
    self.assertTrue(not self.view1.panels['output'].hidden())
  